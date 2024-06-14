#authentication_serice/serializers.py

from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                attrs['user'] = user
            else:
                raise serializers.ValidationError('Invalid username or password.')
        else:
            raise serializers.ValidationError('Both username and password are required.')

        return attrs
    
# authentication/authentication_service/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

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
