from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('art.urls')),
    path('signin/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls'))
]
