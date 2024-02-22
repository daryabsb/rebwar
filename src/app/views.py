from django.shortcuts import get_object_or_404, render
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
    page_title = 'About Us'
    opening = {
        "title": "Know about Orthopaedic Clinic",
        "description": "We are specializes in treatment of Hip, Knee, Shoulder and Regenerative Medicine. Latest medical technology with the state of art medical facility to provide his patients the best possible outcome."
    }

    context = {
        "abouts": abouts,
        "page_crumbs": page_crumbs,
        "opening": opening,
        "page_title": page_title,
    }
    return render(request, "about/index.html", context=context)


def services_view(request):
    services = Service.objects.all().order_by('id')

    page_crumbs = [{"title": "Home", "url": "/"}]
    page_title = 'Services'
    opening = {
        "title": "A wide range of Orthopaedic Treatment",
        "description": "We are specializes in treatment of Hip, Knee, Shoulder and Regenerative Medicine. Latest medical technology with the state of art medical facility to provide his patients the best possible outcome."
    }

    context = {
        "services": services,
        "page_crumbs": page_crumbs,
        "opening": opening,
        "page_title": page_title,
    }
    return render(request, "services/index.html", context=context)


def services_detail_view(request, id):
    from src.core.models import Treatment
    service = get_object_or_404(Service, id=id)
    treatment = Treatment.objects.prefetch_related(
        'conditions', 'procedures').filter(service=service).first()
    page_crumbs = [
        {"title": "Home", "url": "/"},
        {"title": "Services", "url": "/services"},
    ]
    page_title = service.title
    opening = {
        "title": "A wide range of Orthopaedic Treatment",
        "description": "We are specializes in treatment of Hip, Knee, Shoulder and Regenerative Medicine. Latest medical technology with the state of art medical facility to provide his patients the best possible outcome."
    }

    context = {
        "service": service,
        "treatment": treatment,
        "page_crumbs": page_crumbs,
        "opening": opening,
        "page_title": page_title,
    }
    return render(request, "services/detail.html", context=context)

def contact_view(request):
    abouts = About.objects.filter(featured=True).order_by('id')
    page_crumbs = [{"title": "Home", "url": "/"}]
    page_title = 'Contact Us'
    opening = {
        "title": "We are happy to hear from you,",
        "description": "Please contact us using the information below."
    }
    context = {
        "abouts": abouts,
        "page_crumbs": page_crumbs,
        "opening": opening,
        "page_title": page_title,
    }
    return render(request, "contact/index.html", context=context)