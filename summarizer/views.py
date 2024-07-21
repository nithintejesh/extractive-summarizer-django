from django.shortcuts import render
from .forms import URLForm
import requests
import re
import bs4 as bs
import nltk
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

def preprocess_text(text):
    text = re.sub(r'\[[0-9]*\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        parsed_article = bs.BeautifulSoup(response.text, 'html.parser')
        paragraphs = parsed_article.find_all('p')
        article_text = ''.join([p.text for p in paragraphs])
        return preprocess_text(article_text)
    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
    except Exception as e:
        return f"Error parsing the URL content: {e}"

def tokenize_sentences(text):
    return sent_tokenize(text)

def tokenize_words(sentence, stop_words):
    words = word_tokenize(sentence)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word.lower() not in stop_words]

def tf_idf_matrix(sentences, stop_words):
    tf_matrix = {}
    for i, sent in enumerate(sentences):
        tf_table = {}
        words = tokenize_words(sent, stop_words)
        for word in words:
            tf_table[word] = tf_table.get(word, 0) + 1
        total_words = len(words)
        for word in tf_table:
            tf_table[word] = tf_table[word] / total_words
        tf_matrix[i] = tf_table

    idf_matrix = {}
    total_sentences = len(sentences)
    for i in range(total_sentences):
        for word in tf_matrix[i]:
            idf_matrix[word] = idf_matrix.get(word, 0) + 1
    for word in idf_matrix:
        idf_matrix[word] = math.log(total_sentences / float(idf_matrix[word]))

    tf_idf = {i: {word: tf_matrix[i][word] * idf_matrix[word] for word in tf_matrix[i]} for i in tf_matrix}

    return tf_idf

def score_sentences(sentences, tf_idf):
    sentence_scores = {}
    for i, sent in enumerate(sentences):
        score = sum(tf_idf[i].values())
        sentence_scores[sent] = score / len(sent.split())
    return sentence_scores

def generate_summary(sentences, sentence_scores, threshold):
    summary = ""
    for sent in sentences:
        if sentence_scores.get(sent, 0) >= threshold:
            summary += " " + sent
    return summary

def summarize(request):
    summary = ''
    original_length = 0
    summary_length = 0

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            article_text = fetch_web_content(url)
            if article_text.startswith("Error"):
                return render(request, 'summarizer/index.html', {'form': form, 'error': article_text})
            sentences = tokenize_sentences(article_text)
            stop_words = set(stopwords.words("english"))
            tf_idf = tf_idf_matrix(sentences, stop_words)
            sentence_scores = score_sentences(sentences, tf_idf)
            threshold = sum(sentence_scores.values()) / len(sentence_scores)
            summary = generate_summary(sentences, sentence_scores, 1.3 * threshold)
            original_length = len(word_tokenize(article_text))
            summary_length = len(word_tokenize(summary))
    else:
        form = URLForm()

    return render(request, 'summarizer/index.html', {
        'form': form,
        'summary': summary,
        'original_length': original_length,
        'summary_length': summary_length
    })
