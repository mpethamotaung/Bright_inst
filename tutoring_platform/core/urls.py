from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('courses/', views.courses, name='courses'),
    path('index/', views.index, name='index'),
    path('pricing/', views.pricing, name='pricing'),
    path('resources/', views.resources, name='resources'),
    path('signup/', views.signup, name='signup'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('tutor_profile/', views.tutor_profile, name='tutor_profile'),
    path('tutors/', views.tutors, name='tutors'),
]
