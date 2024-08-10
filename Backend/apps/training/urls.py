# apps/training/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainingListCreateAPIView.as_view(), name='training-list-create'),
    path('<int:pk>/', views.TrainingDetailAPIView.as_view(), name='training-detail'),
]
