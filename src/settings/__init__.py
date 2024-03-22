from split_settings.tools import include
from os import environ

ENV = environ.get('DJANGO_ENV') or 'local'

base_settings = [
    'components/paths.py',
    # 'components/storages/conf.py',
    'components/cache.py',
    'components/secretes.py',
    'components/site_settings.py',
    'components/db.py',
    'components/common.py',
    'components/cors.py',
    'components/tinymce.py',
    'components/celery.py',
    'components/redis.py',
]

include(*base_settings)