import os
from pathlib import Path
from django.conf import settings
from src.core.models import Service  # Replace with your actual model
from django.utils.translation import gettext as _


def vendor_files(request):
    # static_dir = settings.BASE_DIR / "static"
    static_dir = Path(settings.STATIC_ROOT)
    # print("vendor_dir/: ", static_dir / "vendor")
    vendor_dir = static_dir / "vendor"
    js_files = [x.relative_to(static_dir) for x in vendor_dir.glob("**/*.js")]
    css_files = [x.relative_to(static_dir) for x in vendor_dir.glob("**/*.css")]
    return {
        "vendor_js_files": js_files,
        "vendor_css_files": css_files,
    }


def get_value(key):
    from src.application.models import Application
    obj = Application.objects.get(key=key)
    return obj.value


def general_data(request):
    from src.contact.models import Contact

    footer_description = get_value('footer_description')
    site_title = "Dr Rebwar : Orthopedic Clinic"
    make_appointment = _("make_appointment")
    welcome_top_line = _("welcome_top_line")

    primary_phone = Contact.objects.filter(
        category='phone', is_primary=True).first()

    phones = Contact.objects.filter(category='phone')
    primary_address = Contact.objects.filter(
        category='address', is_primary=True).first()
    addresses = Contact.objects.filter(category='address')
    emails = Contact.objects.filter(category='email')

    print("{% trans primary_phone %}: ", primary_phone)

    return {
        "site_title": site_title,
        "make_appointment": make_appointment,
        "welcome_top_line": welcome_top_line,
        "top_phone": primary_phone,
        "phones": phones,
        "addresses": addresses,
        "primary_address": primary_address,
        "emails": emails,
        "footer_description": footer_description,
    }


def menu_data(request):
    # Retrieve menu data from the database or any other source
    menu_items = Service.objects.all()  # Replace with your actual query
    # Add the menu data to the context
    return {'menu_items': menu_items}


def menu_items(request):
    from src.core.models import Menu
    # Retrieve all menus with submenus and order them by ordinal
    menus = Menu.objects.filter(
        parent_menu__isnull=True
    ).order_by('ordinal').prefetch_related('submenus')

    # Preload submenus within their parent menus
    # for menu in menus:
    #     menu.submenus = menu.submenus.set().order_by('ordinal')

    return {"menus": menus}


def language_ref(request):
    from src.app.const import LANGUAGES_CHOICES
    rtl = False
    language_code = 'en'
    print(LANGUAGES_CHOICES[0])

    if language_code != 'en':
        rtl = True
    return {'language_code': language_code, 'rtl': rtl}


# def global_settings(request):
#     return {
#         "is_settings": True,
#         "default_duration_type": "month",
#         "terms": TERMS_AND_CONDITIONS,
#     }


# def incomplete_purchases(request):
#     user = request.user
#     if user.is_authenticated:
#         my_invoices, my_invoices_count = user.get_invoices
#         incompletes, incompletes_count = user.incomplete_purchases
#         return {
#             "purchases": incompletes,
#             "my_invoices": my_invoices,
#             "invoices_count": my_invoices_count,
#             "purchases_count": incompletes_count,
#         }
#     return {
#         "purchases": [],
#         "my_invoices": [],
#         "invoices_count": 0,
#         "purchases_count": 0,
#     }


# TERMS_AND_CONDITIONS = [
#     {
#         "header": "General Terms",
#         "body": [
#             "By accessing and ordering from the website, you agree to the Terms of Use.",
#             "AlphaSquad is not responsible for any damages that may occur during use of resources.",
#             "AlphaSquad can change prices and usage policy at any time.",
#         ],
#     },
#     {
#         "header": "Products",
#         "body": [
#             "All products and services are delivered by AlphaSquad.",
#             "Downloads can be accessed from the user's dashboard.",
#         ],
#     },
#     {
#         "header": "Security",
#         "body": [
#             "Payments are processed securely through Gumroad.",
#         ],
#     },
#     {
#         "header": "Cookie Policy",
#         "body": [
#             "The website uses cookies for personalization and tracking referrals.",
#             "Google Analytics is used to analyze website use.",
#             "Deleting cookies will negatively impact the website's usability.",
#         ],
#     },
#     {
#         "header": "Payments",
#         "body": [
#             "Payments are processed through Gumroad, which is compliant with OFAC regulations.",
#             "OFAC restricts shoppers from certain countries.",
#         ],
#     },
#     {
#         "header": "Ownership",
#         "body": [
#             "Ownership is governed by the usage license selected by the seller.",
#         ],
#     },
#     {
#         "header": "Changes to Terms",
#         "body": [
#             "Changes will be posted on the website, and registered users will be notified.",
#         ],
#     },
#     {
#         "header": "Do No Harm",
#         "body": [
#             "Software developers are responsible for the social and environmental impacts of their work.",
#             "The company seeks a just world and will not work with organizations that promote harmful actions.",
#         ],
#     },
#     {
#         "header": "Terms",
#         "body": [
#             "Redistribution and use of the source code and binary forms are permitted under certain conditions.",
#             "The software cannot be used by organizations that promote harmful actions.",
#         ],
#     },
# ]
