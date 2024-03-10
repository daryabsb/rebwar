import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# GDAL_LIBRARY_PATH = 'venv/Lib/site-packages/osgeo/gdal304.dll'

# Static files (CSS, JavaScript, images)
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PROTECTED_MEDIA_ROOT = os.path.join(BASE_DIR, 'protected')
