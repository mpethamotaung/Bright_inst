# tutoring_platform/frontend_service/frontend/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
