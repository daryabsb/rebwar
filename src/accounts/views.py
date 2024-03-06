from django.shortcuts import render
from django.views.generic import ListView, DetailView
from src.accounts.models import DoctorProfile

class DoctorDetailView(DetailView):
    model = DoctorProfile
    template_name = 'doctors/profile.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        from src.accounts.models import TitleChoice, DoctorSchedule
        from src.contact.models import Contact
        context = super().get_context_data(**kwargs)
        # Add additional context variables here
        subjects = TitleChoice.objects.all()
        doctor_resume = []

        for subject in subjects:
            cv = {"title": subject.display, "icon": subject.icon}
            items = []
            for item in subject.titles.all():

                if item.doctor == context['doctor']:
                    items.append(item.description)
            cv["items"] = items
            doctor_resume.append(cv)
        context['resume'] = doctor_resume

        # CONTACT DETAILS
        addresses = Contact.objects.filter(category='address')
        phones = Contact.objects.filter(category='phone')
        emails = Contact.objects.filter(category='email')
        context['addresses'] = addresses
        context['phones'] = phones
        context['emails'] = emails

        schedules = DoctorSchedule.objects.filter(doctor=context['doctor'])
        context['schedules'] = schedules
        return context
