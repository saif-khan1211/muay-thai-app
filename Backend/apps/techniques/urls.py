# apps/training/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TechniquesListCreateAPIView.as_view(), name='techniques-list-create'),
    path('<int:pk>', views.TechniquesDetailAPIView.as_view(), name='techniques-detail'),

]
