from django.db import models
from django.contrib.auth.models import AbstractUser

#User class (Tutor/Student)
class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)

#Subject Class(Generated by Tutor/Staff)
class Subject(models.Model):
    name = models.CharField(max_length=100)

#Session class, regulated Tutor & Student session
class Session(models.Model):
    tutor = models.ForeignKey(User, related_name='tutoring_sessions', on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name='learning_sessions', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()