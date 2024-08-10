from rest_framework import generics, permissions
from .models import Techniques
from .serializers import TechniquesSerializer

class TechniquesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Techniques.objects.all()
    serializer_class = TechniquesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TechniquesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Techniques.objects.all()
    serializer_class = TechniquesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





