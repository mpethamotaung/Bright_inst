#tutoring_platform(sim)/mywebsite/main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #Homepage
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('pricing/', views.pricing, name='pricing'),
    path('resources/', views.resources, name='resources'),
    path('singup/', views.signup, name='signup'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('tutor_profile/', views.tutor_profile, name='tutor_profile'),
    path('tutors/', views.tutors, name='tutors'),
    path('booking/', views.booking, name='booking'),

]