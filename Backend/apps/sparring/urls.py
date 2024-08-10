# apps/training/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SparringListCreateAPIView.as_view(), name='sparring-list-create'),
    path('<int:pk>/', views.SparringDetailAPIView.as_view(), name='sparring-detail')
]
