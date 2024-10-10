from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Artist
from .utils import generate_otp


@receiver(post_save, sender=User)
def save_user(sender, instance, created, **kwarg):
	if created:
		otp = generate_otp()
		artist = Artist.objects.create(user=instance, validate=False)
		artist.otp = otp
		artist.save()
		Token.objects.create(user=instance)