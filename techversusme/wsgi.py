import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techversusme.settings")

application = get_wsgi_application()

# Enable WhiteNoise for caching and static file handling
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
