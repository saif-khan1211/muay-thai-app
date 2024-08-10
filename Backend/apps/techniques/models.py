from django.db import models


class Techniques(models.Model):
    videoLink = models.URLField(max_length=200)
    description = models.TextField()
    title = models.CharField(max_length=250)
    updatedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now=True)
    BOXING = 'boxing'
    KICKING = 'kicking'
    KNEES = 'knees'
    ELBOWS = 'elbows'
    CLINCHING = 'clinching'
    HEAVY_BAG = 'heavy_bag'
    SHADOWBOXING = 'shadowboxing'
    CATEGORY_CHOICES = [
        (BOXING, 'Boxing'),
        (KICKING, 'Kicking'),
        (KNEES, 'Knees'),
        (ELBOWS, 'Elbows'),
        (CLINCHING, 'Clinching'),
        (HEAVY_BAG, 'Heavy Bag'),
        (SHADOWBOXING, 'Shadowboxing'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=BOXING)


