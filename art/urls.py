from django.urls import path
from art import views


urlpatterns = [
    path('posts/', views.PostViewSet.as_view()),
    path('posts/<int:pk>/', views.post_detail),
]
