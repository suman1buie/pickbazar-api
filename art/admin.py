from django.contrib import admin
from art.models import PostImage


class PostImageAdmin(admin.ModelAdmin):
    fields = ['image_title', 'catagory', 'image', 'updated_date', 'uploaded_by', 'descriptions']

admin.site.register(PostImage, PostImageAdmin)
