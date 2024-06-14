# authentication/authentication_service/users/urls.py

from django.urls import path
from .views import UserCreate, UserLogin, UserDetails, UserLogout
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('user-details/', UserDetails.as_view(), name='user-details'), 
    path('logout/', TemplateView.as_view(template_name='logout.html'), name='logout'),
]
