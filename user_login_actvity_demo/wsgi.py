"""
WSGI config for user_login_actvity_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_login_actvity_demo.settings")

application = get_wsgi_application()
application = WhiteNoise(application)
