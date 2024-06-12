# users/urls.py

from django.urls import path
from .views import UserRegistrationView, UserLoginView

# Define URL paths to access the views
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
