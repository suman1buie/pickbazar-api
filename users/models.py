from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.utils.translation import gettext_lazy as _


class Artist(models.Model):
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    place = models.CharField(max_length=50, null=True, blank=True)
    linkedin_profile = models.CharField(max_length=60, null=True, blank=True)
    insta_profile = models.CharField(max_length=60, null=True, blank=True)
    user = models.OneToOneField(to=User, related_name="artists", on_delete=models.CASCADE)
    validate = models.BooleanField(default=False)
    otp = models.CharField(_("OTP"), max_length=5, default="00000")

    def ___str___(self) -> str:
          return self.user.username
      
      