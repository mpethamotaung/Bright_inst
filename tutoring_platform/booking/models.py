from django.db import models
from django.conf import settings


class Appointment(models.Model):
    tutor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tutor_appointments",
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_appointments",
    )
    date = models.DateTimeField()
    duration = models.DurationField()
    subject = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=[("scheduled", "Scheduled"), ("completed", "Completed")]
    )
