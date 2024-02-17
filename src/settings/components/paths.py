from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR.parent / "local-cdn" / "static"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR.parent / "local-cdn" / "media"
PROTECTED_MEDIA_ROOT = BASE_DIR.parent / "local-cdn" / "protected"