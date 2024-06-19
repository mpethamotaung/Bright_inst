# authentication/authentication_service/views.py
from django.shortcuts import render
from rest_framework import status
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserLoginSerializer, TokenRefreshSerializer  # Ensure TokenRefreshSerializer is imported
from rest_framework_simplejwt.tokens import RefreshToken

#User registration class
class UserRegistrationView(View):
    #Get Method: renders registration html when reg page is accessed
    def get(self, request):
        return render(request, 'registration.html')
    #POST Meth: processes form data
    def post(self, request):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'registration.html', {'message': 'User registered successfully.'})
        return render(request, 'registration.html', {'errors': serializer.errors})

#User Login Class
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

class UserLogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)

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

