import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

from django.conf import settings

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR.parent / "local-cdn" / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# print('STATIC_ROOT: ', STATIC_ROOT)
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PROTECTED_MEDIA_ROOT = os.path.join(BASE_DIR, 'protected')
