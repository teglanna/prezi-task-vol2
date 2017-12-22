import os
import dj_database_url

from .base import *

DEBUG = False

# Update database configuration with $DATABASE_URL. (used from Heroku docs)
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
