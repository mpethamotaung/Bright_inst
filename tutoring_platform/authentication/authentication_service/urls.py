"""
URL configuration for authentication_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# authentication/authentication_service/urls.py

from django.contrib import admin
from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, TokenRefreshView, UserLogoutView ,index  # Ensure these imports are here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')), #include users app
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-registration'),  # Registration endpoint
    path('api/auth/login/', UserLoginView.as_view(), name='user-login'),  # Login endpoint
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'), #Continuous logged in endpoint
    path('api/auth/logout/', UserLogoutView.as_view(), name='user-logout'), #Logout endpoint

    #Test code
    path('', index, name='index'),  # Root URL
]




"""URLSs Configuration: defining the URL routes for the user registration endpoint. This connects our urls.py file in 
    users app and inlcudes it in the main project(authentication_service) urls.py to allow user registration endpoint
    to be accessed at '/users/register/' """