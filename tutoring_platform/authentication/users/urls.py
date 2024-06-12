from django.urls import path
from .views import UserCreate
from .import views

#Define url path to access the view
urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
]
