from django.shortcuts import get_object_or_404, render
from src.accounts.models import DoctorProfile, DoctorResume, TitleChoice
from src.core.models import Slide, Service, Journey, About, Testimonial


def get_app_content(app_label, model_name):
    from django.contrib.contenttypes.models import ContentType
    from src.core.models import SectionContent

    app_type = ContentType.objects.get(app_label=app_label, model=model_name)

    app_type_content = SectionContent.objects.filter(
        content_type=app_type).first()
    print("app_type_content = ", app_type_content)
    if app_type_content:
        app_title = app_type_content.title
        app_description = app_type_content.description
    else:
        # Handle the case when the 'About' content is not found
        app_title = None
        app_description = None

    return app_title, app_description


def home_view(request):
    from django.db import models
    from django.db.models import Count, Value
    from django.db.models.functions import Concat
    doctor = DoctorProfile.objects.filter(featured=True).first()
    subjects = TitleChoice.objects.all()
    doctor_resume = []
    for subject in subjects:
        if subject.featured: #  in ['achievement', 'special_expertise', 'member_of_foundation']:
            cv = {"title": subject.display, "icon": subject.icon}
            items = []
            for item in subject.titles.all():
                if item.doctor == doctor:
                    items.append(item.description)
            cv["items"] = items
            doctor_resume.append(cv)

    # doctor_resume_queryset = DoctorResume.objects.filter(doctor=doctor)
    # grouped_resumes = doctor_resume_queryset.values('title').annotate(
    #     title_description_list=Concat('description', Value(
    #         '|'), output_field=models.TextField())
    # )
    # for group in grouped_resumes:
    #     title = group['title']
    #     descriptions_list = group['title_description_list'].split('|')
    #     for description in descriptions_list:
    #         print(f'  Description: {description.strip()}')

    quotes = Testimonial.objects.all()
    slides = Slide.objects.all()
    services = Service.objects.all()
    journeys = Journey.objects.prefetch_related(
        'journey_details').all().order_by('id')

    journey_title, journey_description = get_app_content("core", "journey")
    service_title, service_description = get_app_content("core", "service")
    
    journey_opening = {
        "title": journey_title,
        "description": journey_description
    }
    service_opening = {
        "title": service_title,
        "description": service_description
    }

    context = {
        "doctor": doctor,
        "resume": doctor_resume,
        "slides": slides,
        "quotes": quotes,
        "journeys": journeys,
        "services": services,
        "journey_opening": journey_opening,
        "service_opening": service_opening
    }
    return render(request, "home/index.html", context=context)


def about_view(request):
    from src.core import crumb_home, app_about_us
    abouts = About.objects.filter(featured=True).order_by('id')
    about_title, about_description = get_app_content("core", "about")
    page_crumbs = [{"title": crumb_home, "url": "/"}]
    page_title = app_about_us
    opening = {
        "title": about_title,
        "description": about_description
    }

    context = {
        "abouts": abouts,
        "page_crumbs": page_crumbs,
        "opening": opening,
        "page_title": page_title,
    }
    return render(request, "about/index.html", context=context)


def services_view(request):
    from src.app import view_services_button
    from src.core import crumb_home, app_services
    services = Service.objects.all().order_by('id')
    service_title, service_description = get_app_content("core", "service")

    page_crumbs = [{"title": crumb_home, "url": "/"}]
    page_title = app_services
    opening = {
        "title": service_title,
        "description": service_description
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
