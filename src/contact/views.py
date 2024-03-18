from django.shortcuts import render
from django.views.generic import ListView, DetailView
from src.contact.models import Contact

class BlogDetailView(ListView):
    model = Contact
    template_name = 'contact/index.html'
    context_object_name = 'contact'