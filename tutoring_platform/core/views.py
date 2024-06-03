from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Subject, Session
from .serializers import UserSerializer, SubjectSerializer, SessionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serailizer_class = SessionSerializer