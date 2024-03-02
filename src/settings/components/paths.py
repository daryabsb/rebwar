import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



# Static files (CSS, JavaScript, images)
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PROTECTED_MEDIA_ROOT = os.path.join(BASE_DIR, 'protected')
