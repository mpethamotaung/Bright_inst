#authentication_serice/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_tutor', 'is_student', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid username or password")
            data['user'] = user
        else:
            raise serializers.ValidationError("Both fields are required")
        
        return data

class TokenRefreshSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs['refresh_token']

        try:
            token = RefreshToken(refresh_token)
        except Exception as e:
            raise serializers.ValidationError(str(e))

        if not token.payload.get('token_type') == 'refresh':
            raise serializers.ValidationError('Token is not of type refresh')

        return attrs
