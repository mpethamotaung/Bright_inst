from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]

""" These URLs define endpoints for listing all courses ('/courses/')
    and for performing CRUD operations on individual courses ('/courses/<id>/')"""