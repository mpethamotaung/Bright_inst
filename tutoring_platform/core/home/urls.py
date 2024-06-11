from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

"""This URL pattern maps the root URL to the 'home' view, so visiting
    the base URL of the website will display the homepage"""