


CORS_ALLOWED_ORIGINS = [
    "https://rebwarallaf.com",
    "https://dr.rebwarallaf.com",
    "https://www.rebwarallaf.com",
    "https://dev.rebwarallaf.com",
    'http://127.0.0.1:5501',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\dr.rebwarallaf\.com$",
    r"^https://\w+\dr.rebwarallaf\.com$",
]
CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = [
    'https://rebwarallaf.com', 
    "https://dr.rebwarallaf.com", 
    "https://www.rebwarallaf.com", 
    "https://dev.rebwarallaf.com", 
    'http://127.0.0.1:5501',]

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:8000",
    'http://127.0.0.1:5501',
    "https://rebwarallaf.com",
    "https://www.rebwarallaf.com",
    "https://dev.rebwarallaf.com",
    "https://dr.rebwarallaf.com",

    # add other origins that should be allowed to make requests here
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)