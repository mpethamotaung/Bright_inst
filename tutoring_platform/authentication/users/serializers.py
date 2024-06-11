from rest_framework import serializers
from .models import CustomUser

#create userserializer class to convert user data to and from JSON format, create new users with hashed passwords
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
