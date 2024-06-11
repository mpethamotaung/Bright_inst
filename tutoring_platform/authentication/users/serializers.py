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

"""Serializers in DRF are used to convert complex data types, such as
    querysets and model instances, to native Python data types that can be
    easily rendered into JSON, XML, or other content types. They are also used
    to validate and transform input data when creating or updating models."""