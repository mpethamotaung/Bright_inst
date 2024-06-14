# users/urls.py
from django.urls import path
from .views import UserCreate, UserDetailView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('me/', UserDetailView.as_view(), name='user-detail'), #route URL path
]
