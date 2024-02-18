from django.shortcuts import render
from src.accounts.models import DoctorProfile
from src.core.models import Slide


def home_view(request):
    doctor = DoctorProfile.objects.filter(featured=True).first()
    slides = Slide.objects.all()
    context = {
        "doctor": doctor,
        "slides": slides
    }
    return render(request, "home/index.html", context=context)