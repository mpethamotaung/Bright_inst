from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
