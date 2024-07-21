# Extractive Text Summarizer using Django

An extractive text summarizer built with Django. This application processes textual content and provides summarized versions using extractive summarization techniques.

## Features

- **Extractive Summarization:** Utilizes various methods to generate concise summaries of input text.
- **User Interface:** Simple web interface for interacting with the summarizer.
- **Customizable:** Easy to integrate and customize for different text summarization needs.

## Requirements

- Python 3.x
- Django 4.x
- Additional Python libraries specified in `requirements.txt`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/extractive-summarizer-django.git
    cd extractive-summarizer-django
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

1. **Navigate to the web application** at `http://127.0.0.1:8000/`.
2. **Upload or input your text** into the provided field.
3. **Click "Summarize"** to get the extractive summary.

## Code Examples

To interact with the summarizer programmatically, use the following code snippet:

```python
import requests

url = 'http://127.0.0.1:8000/summarize/'
data = {
    'text': 'Your input text here.'
}

response = requests.post(url, data=data)
summary = response.json()
print(summary)
```

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact:

- **Email:** [nithintejesh@gmail.com](mailto:nithintejesh@gmail.com)
- **GitHub:** [nithintejesh/extractive-summarizer-django](https://github.com/nithintejesh/extractive-summarizer-django)
- **LinkedIn:** [nithintejesh](https://www.linkedin.com/in/nithintejesh)
- **X:** [@nithintejesh](https://x.com/nithintejesh)

Feel free to reach out with any questions or feedback!

