from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'tutor', 'student', 'date', 'duration', 'subject', 'status']

"""Serializers are used to convert complex data types, such as model instances,
    into native Python data types that can be rendered into JSON, 
    XML, or other content types."""