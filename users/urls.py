from rest_framework import routers
from django.urls import path
from users import views

urlpatterns = [
    path('artists/', views.artists_list),
    path('register/', views.register_artist),
    path('verify-otp/', views.verify_otp),
    path('artists/<int:pk>/', views.artist_detail),
    path('users/', views.UserViewSet.as_view()),
    path('delete-user/<int:pk>/',views.delet_user)
]
