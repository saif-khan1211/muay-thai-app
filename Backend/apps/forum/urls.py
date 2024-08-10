from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailAPIView.as_view(), name='categories-detail'),

    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view(), name='post-detail'),

    # URL to get posts by a specific category
    path('categories/<int:category_id>/posts/', views.PostListByCategoryAPIView.as_view(), name='posts-by-category'),

    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', views.CommentDetailAPIView.as_view(), name='comment-detail'),
]
