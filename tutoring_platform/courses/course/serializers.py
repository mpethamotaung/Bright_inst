from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'tutor', 'created_at']

"""Serializers convert the 'course' model instances to and from JSON, making
    it easy to handle API responses and requests"""