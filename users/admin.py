from django.contrib import admin
from users.models import Artist


class ArtistAdmin(admin.ModelAdmin):
    fields = ['bio', 'phone_number', 'place', 'linkedin_profile', 'insta_profile', 'user', 'validate', 'otp']
    

admin.site.register(Artist, ArtistAdmin)
