# Paquetes
django 
pytest==8.0.1
python-dotenv==1.0.1 
djangorestframework==3.14.0
pytest-django-4.8.0

# Comandos
django-admin startproject drfecommerce
manage.py runserver

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key)

## Pytest
pytest -h # prints options _and_ config file settings