from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


#initiate user class to allow users to access this endpoint
class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

