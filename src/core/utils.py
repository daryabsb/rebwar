import os
from pygeoip import GeoIP
from django.conf import settings

MAPS_FOLDER_PATH = os.path.join(settings.PROJECT_PATH, 'core', 'maps')
# geoip_db_path = os.path.join(MAPS_FOLDER_PATH, 'GeoLiteCity.dat')
geoip_db_path = os.path.join(MAPS_FOLDER_PATH, 'maxmind4.dat')

geolocation_data = {
    'dma_code': 0,
    'area_code': 0,
    'metro_code': None,
    'postal_code': None,
    'country_code': 'IQ',
    'country_code3': 'IRQ',
    'country_name': 'Iraq',
    'continent': 'AS',
    'region_code': '01',
    'city': 'Sulaymaniyah',
    'latitude': 34.149699999999996,
    'longitude': 42.3819,
    'time_zone': 'Asia/Baghdad'}

kurdistan_cities = ['erbil', 'sulaymaniyah', 'duhok']

arab_countries = {
    'DZ': 'Algeria',
    'BH': 'Bahrain',
    'KM': 'Comoros',
    'DJ': 'Djibouti',
    'EG': 'Egypt',
    'IQ': 'Iraq',
    'JO': 'Jordan',
    'KW': 'Kuwait',
    'LB': 'Lebanon',
    'LY': 'Libya',
    'MR': 'Mauritania',
    'MA': 'Morocco',
    'OM': 'Oman',
    'PS': 'Palestine',
    'QA': 'Qatar',
    'SA': 'Saudi Arabia',
    'SO': 'Somalia',
    'SD': 'Sudan',
    'SY': 'Syria',
    'TN': 'Tunisia',
    'AE': 'United Arab Emirates',
    'YE': 'Yemen',
}


class GeoLocaleDetector:
    def __init__(self, user_ip):
        self.user_ip = user_ip
        self.kurdistan_cities = ['erbil', 'sulaymaniyah', 'duhok']

    @property
    def arab_countries(self):
        return {
            'DZ': 'Algeria',
            'BH': 'Bahrain',
            'KM': 'Comoros',
            'DJ': 'Djibouti',
            'EG': 'Egypt',
            'IQ': 'Iraq',
            'JO': 'Jordan',
            'KW': 'Kuwait',
            'LB': 'Lebanon',
            'LY': 'Libya',
            'MR': 'Mauritania',
            'MA': 'Morocco',
            'OM': 'Oman',
            'PS': 'Palestine',
            'QA': 'Qatar',
            'SA': 'Saudi Arabia',
            'SO': 'Somalia',
            'SD': 'Sudan',
            'SY': 'Syria',
            'TN': 'Tunisia',
            'AE': 'United Arab Emirates',
            'YE': 'Yemen',
        }

    def detect_locale(self):
        country_code, city = self.get_country_and_city()

        if country_code == 'IQ' and city in self.kurdistan_cities:
            return 'ckb'  # Kurdish
        elif country_code in self.arab_countries:
            return 'ar'  # Arabic
        else:
            return 'en'  # English

    def get_country_and_city(self):
        geoip_db_path = os.path.join(MAPS_FOLDER_PATH, 'GeoLiteCity.dat')
        geoip = GeoIP(geoip_db_path)

        try:
            geolocation_data = geoip.record_by_addr(self.user_ip)
            country_code = geolocation_data.get('country_code', '')
            city = geolocation_data.get('city', '')

            if city is None:
                # If the city is None, return 'ckb'
                return country_code, 'ckb'
            else:
                # If the city is not None, convert to lowercase
                return country_code, city.lower()
        except Exception as e:
            # Handle exceptions (e.g., GeoIPError, KeyError) as needed
            print(f"Error getting geolocation data: {e}")
            return '', ''


def create_message(request, locale):
    from django.contrib import messages
    csrf_token = '{% csrf_token %}'

    arabic_html = f'''<apan dir="rtl">غیر اللغة الی العربیة، <a class="btn-link text-gray-500" href="/{locale}/set_language/" onclick="event.preventDefault();document.getElementById('language-form-ar').submit();" role="button"><strong>انقر هنا</strong></a></apan><br />'''
    english_html = f'''<apan dir="ltr">Change the language to english, <a class="btn-link text-gray-500" href="/{locale}/set_language/" onclick="event.preventDefault();document.getElementById('language-form-en').submit();" role="button"><strong>Click here</strong></a></apan><br />'''
    kurdish_html = f'''<apan dir="rtl">زمانەکە بگۆڕە بۆ کوردی، <a class="btn-link text-gray-500" href="/{locale}/set_language/" onclick="event.preventDefault();document.getElementById('language-form-ckb').submit();" role="button"><strong>لێرە کلیک بکە</strong></a></apan>'''

    messages.info(request, '''
    <div id="lang-message" class="alert aler text-center col-lg-6 col-lg-offset-3"
        style="position: fixed; bottom: 20px; z-index: 10; color:black; background-color: rgba(255, 255, 255, 1);box-shadow: 5px 5px 5px gray;border: solid 1px gray;"
        role="alert">
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
            {}{}{}
    </div>'''.format(
        english_html if locale != 'en' else '',
        arabic_html if locale != 'ar' else '',
        kurdish_html if locale != 'ckb' else ''
    )
    )
    # messages.info(
    # request, '''
    # <div class="alert alert-success alert-dismissible fixed-bottom-messages" role="alert">
    #         {}{}{}
    #         <button type="button" class="close position-absolute" data-dismiss="alert" aria-label="Close">
    #             <span aria-hidden="true">&times;</span>
    #         </button>
    #     </div>
    #     '''.format(
    #         english_html if locale != 'en' else '',
    #         arabic_html if locale != 'ar' else '',
    #         kurdish_html if locale != 'ckb' else ''
    #     )
    # )


'''
NO NEED, DELETE LATER

    def get_geolocation_data(self, ip):
        # Path to the GeoIP database file

        geoip_db_path = os.path.join(MAPS_FOLDER_PATH, 'GeoLiteCity.dat')

        # Create a GeoIP object
        geoip = GeoIP(geoip_db_path)

        # Get geolocation information for the given IP
        geolocation_data = geoip.record_by_addr(ip)

        return geolocation_data
'''
