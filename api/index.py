import os
from django.core.wsgi import get_wsgi_application

# 👇 CHANGE THIS to your actual Django project folder name
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "abhi_portfolio.settings"
)

application = get_wsgi_application()
