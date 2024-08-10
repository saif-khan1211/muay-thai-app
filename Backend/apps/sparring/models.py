from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Sparring(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    opponent = models.CharField(max_length=100)
    date = models.DateTimeField()
    duration = models.CharField(max_length=50)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
