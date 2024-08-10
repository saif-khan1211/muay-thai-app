from django.db import models
from django.conf import settings


class Training(models.Model):
    TRAINING_TYPES = [
        ('Muay Thai', 'Muay Thai'),
        ('HIIT Training', 'HIIT Training'),
        ('Shadow Boxing', 'Shadow Boxing'),
        ('Heavy Bag', 'Heavy Bag'),
        ('Running', "Running"),
        ('Weight Lifting', 'Weight Lifting'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    training_type = models.CharField(max_length=50, choices=TRAINING_TYPES)
    duration = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()  # Date of training session
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
