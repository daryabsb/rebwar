from django.shortcuts import render
from src.accounts.models import DoctorProfile
from src.core.models import Slide, Service, Journey, About


def home_view(request):
    doctor = DoctorProfile.objects.filter(featured=True).first()
    slides = Slide.objects.all()
    services = Service.objects.all()
    journeys = Journey.objects.prefetch_related(
        'journey_details').all().order_by('id')

    context = {
        "doctor": doctor,
        "slides": slides,
        "journeys": journeys,
        "services": services
    }
    return render(request, "home/index.html", context=context)


def about_view(request):
    abouts = About.objects.filter(featured=True).order_by('id')
    page_crumbs = [{"title": "Home", "url": "/"}]

    opening = {
        "title": "Know about Orthopaedic Clinic",
        "description": "We are specializes in treatment of Hip, Knee, Shoulder and Regenerative Medicine. Latest medical technology with the state of art medical facility to provide his patients the best possible outcome."
    }

    context = {
        "abouts": abouts,
        "page_crumbs": page_crumbs,
        "opening": opening,
    }
    return render(request, "about/index.html", context=context)
