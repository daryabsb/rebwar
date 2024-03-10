import os
from pygeoip import GeoIP
from django.conf import settings
from django.middleware.locale import LocaleMiddleware
from django.utils import translation
from django.urls import reverse

MAPS_FOLDER_PATH = os.path.join(settings.PROJECT_PATH, 'core', 'maps')

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


# def choose_language_code(raw_offset):
#     # Your logic for choosing a language code based on the raw offset
#     # Example: For positive raw offsets, use 'en' (English), for negative raw offsets, use 'fr' (French)
#     return 'en' if raw_offset >= 0 else 'fr'


# def create_mapping_from_txt(file_path):
#     country_locale_mapping = {}

#     try:
#         with open(file_path, 'r') as txt_file:
#             # Skip the header line
#             next(txt_file)

#             for line in txt_file:

#                 country_code, time_zone, gmt_offset, dst_offset, raw_offset = line.strip().split('\t')
#                 print("country_code = ", country_code, time_zone, raw_offset)

#                 # Choose language code based on your criteria
#                 # For example, you can use a specific language for regions with a certain offset
#                 language_code = choose_language_code(float(raw_offset))

#                 # Add the mapping to the dictionary
#                 country_locale_mapping[country_code] = language_code
#     except (FileNotFoundError, ValueError):
#         # Handle file not found or invalid data format
#         pass

#     return country_locale_mapping

# def get_locale_from_country_code(country_code):
#     # Simple dictionary mapping country codes to language codes
#     tz_info_path = os.path.join(MAPS_FOLDER_PATH, 'timeZones.txt')
#     country_locale_mapping = create_mapping_from_txt(tz_info_path)

#     # Get the locale from the mapping, defaulting to 'en_US' if not found
#     locale = country_locale_mapping.get(country_code, 'en_US')

#     return locale


def get_locale_from_geolocation(geolocation_data):
    # Extract the country code from the geolocation data
    country_code = geolocation_data.get('country_code')
    if country_code in arab_countries:
        locale = 'ar'
    else:
        locale = 'en'
    return locale


class GeoIPMiddleware(LocaleMiddleware):

    def get_locale(self, request):
        from django.utils import translation
        # Get the user's IP address from the request
        user_ip = self.get_client_ip(request)
        # Use pygeoip to get geolocation information
        geolocation_data = self.get_geolocation_data('86.96.239.132')  # DUBAI
        # geolocation_data = self.get_geolocation_data(
        #     '192.44.242.19')  # STOCKHOLM
        # geolocation_data = self.get_geolocation_data(user_ip)
        locale = get_locale_from_geolocation(geolocation_data)

        return locale

    def process_request(self, request):

        locale = self.get_locale(request)
        language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = translation.get_language()

        language = translation.get_language_from_request(request)
        print(language, "==", locale)
        print(language != locale)
        if language != locale:
            translation.activate(locale)
            request.LANGUAGE_CODE = translation.get_language()

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_geolocation_data(self, ip):
        # Path to the GeoIP database file

        geoip_db_path = os.path.join(MAPS_FOLDER_PATH, 'GeoLiteCity.dat')

        # Create a GeoIP object
        geoip = GeoIP(geoip_db_path)

        # Get geolocation information for the given IP
        geolocation_data = geoip.record_by_addr(ip)

        return geolocation_data


'''
geolocation_data =  {
    'dma_code': 0, 
    'area_code': 0, 
    'metro_code': None, 
    'postal_code': None, 
    'country_code': 'AE', 
    'country_code3': 'ARE', 
    'country_name': 'United Arab Emirates', 
    'continent': 'AS', 
    'region_code': '03', 
    'city': 'Dubai', 
    'latitude': 25.258199999999988, 
    'longitude': 55.3047, 
    'time_zone': 'Asia/Dubai'
    }
'''
request = [
    'COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__',
    '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__',
    '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__',
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding',
    '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers',
    '_load_post_and_files', '_mark_post_parse_error', '_read_started', '_set_content_type_params',
    '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body',
    'build_absolute_uri', 'close', 'content_params', 'content_type', 'encoding', 'environ',
    'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers']
request = {
    'ACLOCAL_PATH': 'C:\\Program Files\\Git\\mingw64\\share\\aclocal;C:\\Program Files\\Git\\usr\\share\\aclocal',
    'ACTIVE_CELERY': '1', 'ALLOWED_HOST': '*', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\DaryaIbrahim\\AppData\\Roaming',
    'APPLICATION_INSIGHTS_NO_DIAGNOSTIC_CHANNEL': '1', 'AWS_S3_ACCESS_KEY_ID': 'AKIA5VDXRIQHHS5CJQI6',
    'AWS_S3_SECRET_ACCESS_KEY': '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', 'AWS_STORAGE_BUCKET_NAME': 'aron-neon',
    'BASE_ENDPOINT': 'http://127.0.0.1:8000', 'CELERY_BROKER_DB': '1', 'CELERY_RESULT_DB': '2',
    'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_14700_LJORLSDBAHAFSAYR', 'COLORTERM': 'truecolor',
    'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
    'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-V9VCDNO', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
    'CONFIG_SITE': 'C:/Program Files/Git/etc/config.site', 'DATABASE_HOST': '86.96.239.197', 'DATABASE_NAME': 'allaf_db',
    'DATABASE_PASSWORD': 'postgres2019', 'DATABASE_PORT': '5432',
    'DATABASE_URL': 'postgres://postgres:postgres2019@database.ticqc.ae:5433/allaf_gis',
    'DATABASE_URL_BAK': 'postgres://daryabsb:y7XzKikRpd8u@ep-steep-sky-26709496.ap-southeast-1.aws.neon.tech/neondb',
    'DATABASE_URL_MAIN': 'postgres://daryabsb:y7XzKikRpd8u@ep-silent-lab-515392.ap-southeast-1.aws.neon.tech/neondb',
    'DATABASE_USER': 'postgres', 'DISPLAY': 'needs-to-be-defined', 'DJANGO_DEBUG': '1',
    'DJANGO_SECRET_KEY': 'django-insecure-(q3)w+fzzwwc616scd%9q*iuwfnkd6jec8n24y*!51gx*tt4z0',
    'DJANGO_SETTINGS_MODULE': 'src.settings', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EXEPATH': 'C:\\Program Files\\Git\\bin',
    'FERNET_KEY': 'T24ZnzCnFpyX_YCF38j-tZ-9kWXvyL-9ym0Z-0aW0Gs=', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',
    'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
    'GIT_ASKPASS': 'c:\\Users\\DaryaIbrahim\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh',
    'GIT_EDITOR': '"c:\\Users\\DaryaIbrahim\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\git-editor.sh"',
    'HOME': 'C:\\Users\\DaryaIbrahim', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\DaryaIbrahim', 'HOSTNAME': 'DESKTOP-V9VCDNO', 'HOST_ENV': 'home',
    'INFOPATH': 'C:\\Pnfo;C:\\Program Files\\Git\\usr\\info;C:\\Program Files\\Git\\share\\info',
    'INTEL_DEV_REDIST': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\',
    'LANG': 'en_US.UTF-8', 'LOCALAPPDATA': 'C:\\Users\\DaryaIbrahim\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-V9VCDNO',
    'MANPATH': 'C:\\Program Files Fil Files\\Git\\usr\\man;C:\\Program Files\\Git\\share\\man',
    'MIC_LD_LIBRARY_PATH': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Libraries\\compiler\\lib\\mic',
    'MINGW_CHOST': 'x86_64-w64-mingw32', 'MINGW_PACKAGE_PREFIX': 'mingw-w64-x86_64', 'MINGW_PREFIX': 'C:/Program Files/Git/mingw64',
    'MSYSTEM': 'MINGW64', 'MSYSTEM_CARCH': 'x86_64', 'MSYSTEM_CHOST': 'x86_64-w64-mingw32', 'MSYSTEM_PREFIX': 'C:/Program Files/Git/mingw64',
    'NUMBER_OF_PROCESSORS': '12', 'NVM_HOME': 'C:\\Users\\DaryaIbrahim\\AppData\\Roaming\\nvm',
    'NVM_SYMLINK': 'C:\\Program Files\\nodejs', 'ONEDRIVE': 'C:\\Users\\DaryaIbrahim\\OneDrive',
    'ORIGINAL_PATH': 'C:am .dotnet\\toaming\\nvm;C:\\Program Files\\nodejs;C:\\Users\\DaryaIbrahim\\AppData\\Roaming\\npm',
    'ORIGINAL_TEMP': 'C:/Users/DARYAI~1/AppData/Local/Temp', 'ORIGINAL_TMP': 'C:/Users/DARYAI~1/AppData/Local/Temp',
    'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'OS': 'Windows_NT',
    'PATH': 'C:\\Program Files\\Git\\usr\\bin\\core_perl',
    'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',
    'PKG_CONFIG_PATH': 'C:\\Program Files\\Git\\mingw64\\lib\\pkgconfig;C:\\Program Files\\Git\\mingw64\\share\\pkgconfig',
    'PLINK_PROTOCOL': 'ssh', 'PROCESSOR_ARCHITECTURE': 'AMD64',
    'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel',
    'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a',
    'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files',
    'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files',
    'PROMPT': '(venv) $P$G',
    'PS1': '(venv) \\[\\033w\\[\\033[36m\\]`__git_ps1`\\[\\033[0m\\]\\n$ ',
    'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
    'PUBLIC': 'C:\\Users\\Public', 'PWD': 'E:/api/rebwar',
    'PYTHONIOENCODING': 'utf-8',
    'PYTHONUSERBASE': 'C:\\Users\\DaryaIbrahim\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages',
    'REDIS_HOST': '127.0.0.1', 'REDIS_PORT': '6379',
    'RUN_MAIN': 'true', 'SESSIONNAME': 'Console',
    'SHELL': 'C:\\Program Files\\Git\\usr\\bin\\bash.exe',
    'SHLVL': '1', 'SSH_ASKPASS': 'C:/Program Files/Git/mingw64/bin/git-askpass.exe',
    'STRIPE_SECRET_KEY': 'sk_test_51MsrPcC4r4VDMvXgrRcXszZYwEOjjJuNfqX0HYHHGvdV2gDdoUEtwYJHk679yS5JtVUHxGjLqhRNCYoeJHsnFaKa00hY8ZeQYC',
    'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\DARYAI~1\\AppData\\Local\\Temp',
    'TERM': 'xterm-256color', 'TERM_PROGRAM': 'vscode', 'TERM_PROGRAM_VERSION': '1.87.1',
    'TMP': 'C:\\Users\\DARYAI~1\\AppData\\Local\\Temp', 'TMPDIR': 'C:\\Users\\DARYAI~1\\AppData\\Local\\Temp',
    'USERDOMAIN': 'AzureAD', 'USERDOMAIN_ROAMINGPROFILE': 'AzureAD', 'USERNAME': 'DaryaIbrahim',
    'USERPROFILE': 'C:\\Users\\DaryaIbrahim', 'VIRTUAL_ENV': 'E:\\api\\rebwar\\venv',
    'VIRTUAL_ENV_PROMPT': '(venv) ', 'VSCODE_ENV_PREPEND': 'PATH=E\\x3a\\api\\rebwar\\venv\\Scripts;',
    'VSCODE_ENV_REPLACE': 'ACTxeFoundation.Python.3.11_qbz5n2kfra8p0\\LocalCache\\local-packages',
    'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '',
    'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Ut\\dist\\askpass-main.js',
    'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\DaryaIbrahim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'VSCODE_GIT_EDITOR_EXTRA_ARGS': '',
    'VSCODE_GIT_EDITOR_MAIN': 'c:\\Uset\\git-editor-main.js',
    'VSCODE_GIT_EDITOR_NODE': 'C:\\Users\\DaryaIbrahim\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
    'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-cd79dd3129-sock',
    'WINDIR': 'C:\\Windows',
    'WS_ENDPOINT': 'ws://127.0.0.1:8000', 'ZES_ENABLE_SYSMAN': '1', '_': '\\api\\rebwar\\venv/Scripts/python',
    '_OLD_VIRTUAL_PROMPT': '$P$G', 'SERVER_NAME': 'activation.easeus.com',
    'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '',
    'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1',
    'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET',
    'PATH_INFO': '/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain',
    'HTTP_HOST': '127.0.0.1:8000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0',
    'HTTP_SEC_CH_UA': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_SEC_CH_UA_PLATFORM': '"Windows"', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'HTTP_SEC_FETCH_SITE': 'same-origin',
    'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_REFERER': 'http://127.0.0.1:8000/',
    'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br, zstd', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9',
    'HTTP_COOKIE': '_ga=9699203 sessionid=d4i8wf2fnhyzbefeq1ioldo6skwhytgc; django_language=en',
    'wsgi.input': 'django.core.handlers.wsgi.LimitedStream object at 0x00000269D19B68F0>',
    'wsgi.errors': 'io.TextIOWrapper name=<stderr> mode=w encoding=utf-8>',
    'wsgi.version': (1, 0),
    'wsgi.run_once': False, 'wsgi.url_scheme': 'http',
    'wsgi.multithread': True,
    'wsgi.multiprocess': False,
    'wsgi.file_wrapper': '<class wsgiref.util.FileWrapper'}

request_headers = {
    'Content-Length': '',
    'Content-Type': 'text/plain',
    'Host': '127.0.0.1:8000',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'http://127.0.0.1:8000/',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': '''
    _ga=GA1.1.783538621.1675775062;
    _ga_HZMY0VC7VL=GS1.1.1675775061.1.1.1675775128.0.0.0;
    __utma=96992031.783538621.1675775062.1675839225.1675839225.1;
    __utmc=96992031; tabstyle=html-tab;
    _fbp=fb.3.1708157066782.429758719;
    _ga_BFXQ97M871=GS1.1.1708235629.2.0.1708235629.60.0.0; 
    csrftoken=d3muXAsIaEnCLyuLIAIw7In3OGmj1kcr;
    sessionid=d4i8wf2fnhyzbefeq1ioldo6skwhytgc;
    django_language=en
    '''
}

response = [
    '__bytes__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
    '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
    '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_charset', '_container', '_content_type_for_repr', '_handler_class',
    '_reason_phrase', '_resource_closers',
    'charset', 'close', 'closed', 'content', 'cookies', 'delete_cookie', 'flush', 'get', 'getvalue',
    'has_header', 'headers', 'items', 'make_bytes', 'readable', 'reason_phrase', 'seekable', 'serialize',
    'serialize_headers', 'set_cookie', 'set_signed_cookie', 'setdefault', 'status_code', 'streaming', 'tell', 'writable',
    'write', 'writelines']

request = [
    'COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__',
    '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
    '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',

    '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host',
    '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error',
    '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers',

    'accepted_types',
    'accepts',
    'body',
    'build_absolute_uri',
    'close',
    'content_params',
    'content_type',
    'encoding',
    'environ',
    'get_full_path',
    'get_full_path_info',
    'get_host',
    'get_port',
    'get_signed_cookie',
    'headers',
    'is_secure',
    'method',
    'parse_file_upload',
    'path',
    'path_info',
    'read',
    'readline',
    'readlines',
    'resolver_match',
    'scheme',
    'session',
    'upload_handlers'
]

request_headers2 = {
    'Content-Length': '', 'Content-Type': 'text/plain', 'Host': '127.0.0.1:8000',
    'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows Natication/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'http://127.0.0.1:8000/',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9', 'Cookie': 'csrftoken=CoV2Em7V2hDUlb3LS8d85EnsBjgnRirG; django_language=en-US'}
