import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

from django.conf import settings

# Static files (CSS, JavaScript, images)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PROTECTED_MEDIA_ROOT = os.path.join(BASE_DIR, 'protected')

print("STATIC_ROOT: ", STATIC_ROOT)
