# authentication_service/views.py

#User registration imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer

#User login imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


#User registration View
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#User login view
class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # User authenticated, generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({"message": "User logged in successfully.", "access_token": str(refresh.access_token)}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({"message": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)
