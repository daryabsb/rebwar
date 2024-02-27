import os
from pathlib import Path
from django.conf import settings
from src.core.models import Service  # Replace with your actual model


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

def general_data(request):
    site_title = "Dr Rebwar : Orthopedic Clinic"

    return {
        "site_title": site_title
    }


def menu_data(request):
    # Retrieve menu data from the database or any other source
    menu_items = Service.objects.all()  # Replace with your actual query
    # Add the menu data to the context
    return {'menu_items': menu_items}


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
