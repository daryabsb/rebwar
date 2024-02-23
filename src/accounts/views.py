from django.shortcuts import render
from django.views.generic import ListView, DetailView
from src.accounts.models import DoctorProfile

class DoctorDetailView(DetailView):
    model = DoctorProfile
    template_name = 'doctors/profile.html'
    context_object_name = 'doctor'