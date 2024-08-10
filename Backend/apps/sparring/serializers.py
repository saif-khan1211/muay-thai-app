from .models import Sparring
from rest_framework import serializers


class SparringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sparring
        fields = ['id', 'opponent', 'date', 'duration', 'notes']
