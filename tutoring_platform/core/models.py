from django.db import models
from django.contrib.auth.models import AbstractUser

#User class (Tutor/Student)
class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=True)


