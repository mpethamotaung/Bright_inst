# shared_assets/assets/urls.py

from django.urls import path
from .views import base

urlpatterns = [
    path('', base, name='base'),
]

"""This URL pattern maps the root URL ('') to the base view function.
    So, when user visits the root URL of shared assets service, the base
    view will be called to render the base.html template"""