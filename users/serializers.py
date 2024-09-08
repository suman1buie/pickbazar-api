from django.contrib.auth.models import User
from users.models import Artist
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Artist
        fields = ['bio', 'phone_number', 'place', 'linkedin_profile', 'user', 'user_id', 'insta_profile']



 