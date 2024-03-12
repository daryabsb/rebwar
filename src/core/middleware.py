from django.middleware.locale import LocaleMiddleware
from django.utils import translation
from django.contrib import messages
from django.conf import settings


# user_ip = '62.201.217.174'  # SLEMANI
# user_ip = '130.193.241.255'  # ERBIL
# user_ip = '86.96.239.132'  # DUBAI
# user_ip = '192.44.242.19'  # STOCKHOLM
class GeoIPMiddleware(LocaleMiddleware):

    def get_locale(self, request):
        from src.core.utils import GeoLocaleDetector
        # Get the user's IP address from the request
        user_ip = self.get_client_ip(request)
        # user_ip = '62.201.217.174'  # SLEMANI
        # user_ip = '130.193.241.255'  # ERBIL
        # user_ip = '86.96.239.132'  # DUBAI
        # user_ip = '192.44.242.19'  # STOCKHOLM
        locale_detector = GeoLocaleDetector(user_ip)
        locale = locale_detector.detect_locale()
        return locale

    def process_request(self, request):
        from src.core.utils import create_message
        user_prefered_lang = request.COOKIES.get('locale', None)
        language = request.COOKIES.get('django_language', None)

        if language is not None:
            translation.activate(language)
            request.LANGUAGE_CODE = translation.get_language()
            return

        elif user_prefered_lang is not None:
            translation.activate(user_prefered_lang)
            request.LANGUAGE_CODE = translation.get_language()
            return


        elif language is None and user_prefered_lang is None:
            locale = self.get_locale(request)
            request.session['locale_modified'] = True
            request.session['locale'] = locale
            # Activate the detected locale
            translation.activate(locale)
            request.LANGUAGE_CODE = translation.get_language()
            create_message(request, locale)

    def process_response(self, request, response):
        # Check if the locale was modified
        locale_modified = request.session.pop('locale_modified', False)
        locale = request.session.pop('locale', None)

        if locale_modified and locale is not None:
            # Add a message to the user
            response.set_cookie(
                'locale_modified',
                False,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
                secure=settings.LANGUAGE_COOKIE_SECURE,
                httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
                samesite=settings.LANGUAGE_COOKIE_SAMESITE,
            )
            response.set_cookie(
                'locale',
                locale,
                max_age=settings.LANGUAGE_COOKIE_AGE,
                path=settings.LANGUAGE_COOKIE_PATH,
                domain=settings.LANGUAGE_COOKIE_DOMAIN,
                secure=settings.LANGUAGE_COOKIE_SECURE,
                httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
                samesite=settings.LANGUAGE_COOKIE_SAMESITE,
            )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
