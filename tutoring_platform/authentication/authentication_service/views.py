# authentication_service/views.py

# Necessary imports for user registration
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserLoginSerializer  # Ensure you import both serializers

# Necessary imports for user login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# User registration view
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)  # Use UserSerializer here
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User login view
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User logged in successfully.",
                "access_token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
