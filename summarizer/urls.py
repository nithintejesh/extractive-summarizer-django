from django.urls import path
from . import views

app_name = 'summarizer'

urlpatterns = [
    path('', views.summarize, name='summarize'),
]
