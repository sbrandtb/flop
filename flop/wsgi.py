"""
WSGI config for flop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flop.local_settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

application = get_wsgi_application()