from django.shortcuts import render

from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

"""These views use Django Rest Framework's generic views to 
    handle listing, creating, retrieving, updating, and 
    deleting courses."""