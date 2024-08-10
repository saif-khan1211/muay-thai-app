from rest_framework import serializers
from .models import Training


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'training_type', 'duration', 'notes', 'date']
