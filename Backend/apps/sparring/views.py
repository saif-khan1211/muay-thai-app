from .models import Sparring
from .serializers import SparringSerializer
from rest_framework import generics, permissions


class SparringListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sparring.objects.all()
    serializer_class = SparringSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class SparringDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sparring.objects.all()
    serializer_class = SparringSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
