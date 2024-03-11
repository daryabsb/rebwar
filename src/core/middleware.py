from django.middleware.locale import LocaleMiddleware
from django.utils import translation
from django.contrib import messages
from src.core.utils import GeoLocaleDetector
from django.conf import settings


# user_ip = '62.201.217.174'  # SLEMANI
# user_ip = '130.193.241.255'  # ERBIL
# user_ip = '86.96.239.132'  # DUBAI
# user_ip = '192.44.242.19'  # STOCKHOLM
class GeoIPMiddleware(LocaleMiddleware):

    def get_locale(self, request):
        # Get the user's IP address from the request
        # user_ip = self.get_client_ip(request)
        user_ip = '86.96.239.132'
        locale_detector = GeoLocaleDetector(user_ip)
        locale = locale_detector.detect_locale()
        return locale

    def process_request(self, request):
        user_prefered_lang = request.COOKIES.get('locale', None)
        language = request.COOKIES.get('django_language', None)

        if user_prefered_lang is not None or language is not None:
            # translation.activate(user_prefered_lang)
            # request.LANGUAGE_CODE = translation.get_language()
            return

        locale = self.get_locale(request)

        print("language is None = ", language is None and language !=
              locale and user_prefered_lang is None)
        if language is None and language != locale and user_prefered_lang is None:
            request.session['locale_modified'] = True
            request.session['locale'] = locale
            # Activate the detected locale
            translation.activate(locale)
            request.LANGUAGE_CODE = translation.get_language()

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

            messages.info(
                request, '''
                    <div class="alert alert-dismissible" role="alert">
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                        <strong>Your first visit to Dr Rebwar Allaf Clinic website</strong> <br />
                        We served the language based on your location. You can choose other available languages.
                    </div>
                '''
            )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
