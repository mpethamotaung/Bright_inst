# authentication/authentication_service/users/views.py

from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

#User Profile imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView

#User templates navigation imports
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

#Add an endpoint to retrive user details.
#This allows authenticated users to get their profile information
class UserCreate(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
        return render(request, 'register.html', {'errors': serializer.errors})

class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session['refresh_token'] = str(refresh)
            return redirect('user-details')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

class UserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return render(request, 'user_details.html', {'user': user})

class UserLogout(View):
    def get(self, request):
        return render(request, 'logout.html')

    def post(self, request):
        refresh_token = request.session.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        logout(request)
        return redirect('login')

