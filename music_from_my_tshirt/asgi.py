"""ASGI configuration."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music_from_my_tshirt.settings")

application = get_asgi_application()
