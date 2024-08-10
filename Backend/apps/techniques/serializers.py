from rest_framework import serializers
from .models import Techniques


class TechniquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techniques
        fields = ['id','videoLink','description','title','updatedAt','createdAt','category']

