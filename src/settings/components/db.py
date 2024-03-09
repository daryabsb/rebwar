from src.settings.components.env import config
import dj_database_url
from src.settings.components import PROJECT_PATH, BASE_DIR


DATABASE_URL = config("DATABASE_URL", default=None)
# DATABASE_URL = "postgres://postgres:postgres2019@database.ticqc.ae:5433/allaf_gis"
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
    DATABASE_NAME = config("DATABASE_NAME", default='allaf_db')
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

# else:

#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': PROJECT_PATH + 'db.sqlite3',
#         }
#     }
