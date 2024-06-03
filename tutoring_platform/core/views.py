from django.shortcuts import render

from rest_framework import viewsets
from .models import User, Subject, Session
from .serializers import UserSerializer, SubjectSerializer, SessionSerializer

