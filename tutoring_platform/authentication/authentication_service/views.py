# authentication/authentication_service/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserLoginSerializer, TokenRefreshSerializer  # Ensure TokenRefreshSerializer is imported
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Return tokens in response
            return Response({
                'message': 'User logged in successfully.',
                'access_token': access_token,
                'refresh_token': refresh_token
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenRefreshView(APIView):
    def post(self, request):
        serializer = TokenRefreshSerializer(data=request.data)
        if serializer.is_valid():
            # Access the validated data and process the refresh token
            refresh_token = serializer.validated_data['refresh_token']
            try:
                token = RefreshToken(refresh_token)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            # If everything is valid, return a new access token
            return Response({
                'access_token': str(token.access_token)
            }, status=status.HTTP_200_OK)

        # If serializer validation fails, return the validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Test code:
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Authentication Service!")
