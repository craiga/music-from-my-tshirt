"""
WSGI configuration.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music_from_my_tshirt.settings")

application = get_wsgi_application()
