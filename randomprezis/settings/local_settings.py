import os

from .base import *

DEBUG = True

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = 'http://localhost:8888/media/'
