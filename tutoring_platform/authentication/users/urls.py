# users/urls.py

from django.urls import path
from .views import UserCreate, UserLoginView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'), #User registration
    path('login/', UserLoginView.as_view(), name='user-login'), #User login
]
