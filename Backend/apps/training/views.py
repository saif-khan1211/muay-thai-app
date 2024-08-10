from rest_framework import generics, permissions
from .models import Training
from .serializers import TrainingSerializer


class TrainingListCreateAPIView(generics.ListCreateAPIView):
    querySet = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.querySet.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TrainingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
