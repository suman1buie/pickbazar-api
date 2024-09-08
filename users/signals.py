from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Artist


@receiver(post_save, sender=User)
def save_user(sender, instance, created, **kwarg):
	if created:
		Artist.objects.create(user=instance)
		Token.objects.create(user=instance)