from django.utils.translation import gettext as _

def get_value(key):
    from src.application.models import Application
    obj = Application.objects.get(key=key)
    return obj.value

# BUTTONS

global_variables = {
    "buttons": {
        "view_services_button": get_value("view_services_button"),
        "view_profile_button": get_value("view_profile_button"),
        "confirm_appt_button": get_value("confirm_appt_button"),
        "subscribe_button": get_value("subscribe_button"),
        "watch_video_button": get_value("watch_video_button"),
        "more_locations_button": get_value("more_locations_button"),
    },
    "labels": {
        "patients_educations_videos": get_value("patients_educations_videos"),
        "patients_educations_videos_description": get_value("patients_educations_videos_description"),
        "patients_what_say": get_value("patients_what_say"),
        "locations_and_directions": get_value("locations_and_directions"),
        "patient_resources": get_value("patient_resources"),
        "patients_form": get_value("patients_form"),
        "your_first_visit": get_value("your_first_visit"),
        "instruction_after_op": get_value("instruction_after_op"),
        "patients_education": get_value("patients_education"),
        "quick_links": get_value("quick_links"),
        "serve_we_area": get_value("serve_we_area"),
        "subscribe_the_newsletter": get_value("subscribe_the_newsletter"),
        "subscribe_the_newsletter_descrition": get_value("subscribe_the_newsletter_descrition"),
        "write_email_address_placeholder": get_value("write_email_address_placeholder"),
        "footer_bottom_text": get_value("footer_bottom_text"),
        "booking_appointment": get_value("booking_appointment"),
        "crumb_home": get_value("crumb_home"),
        "app_services": get_value("app_services"),
        "app_abount_us": get_value("app_abount_us"),
        "app_blogs": get_value("app_blogs"),
        "footer_description": get_value("footer_description"),
    }
}
