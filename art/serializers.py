# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PostImage
from users.serializers import ArtistSerializer
from users.models import Artist

class PostSerilizer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField(read_only = True)
    uploaded_by = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    # image = serializers.ImageField(required=False)

    class Meta:
        model = PostImage
        fields = ['image_title', 'catagory', 'updated_date', 'artist', 'uploaded_by', 'descriptions', 'image_url']

    def create(self, validated_data):
        return PostImage.objects.create(**validated_data)
    
    def get_artist(self, obj):
        return {
            'id': obj.uploaded_by.id,
            'username': obj.uploaded_by.user.username,
            'last_login': obj.uploaded_by.user.last_login,
            'is_superuser': obj.uploaded_by.user.is_superuser,
        }