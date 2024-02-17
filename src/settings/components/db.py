from src.settings.components.env import config
import dj_database_url

DATABASE_URL = config("B1_DATABASE_URL", default=None)
HOST_ENV = config('HOST_ENV', default='office')

if DATABASE_URL is not None:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True
        )
    }
else:
    DATABASE_NAME = config("DATABASE_NAME")
    DATABASE_USER = config("DATABASE_USER")
    DATABASE_PASSWORD = config("DATABASE_PASSWORD")
    DATABASE_HOST = config("DATABASE_HOST")
    DATABASE_PORT = config("DATABASE_PORT")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
        }
    }
