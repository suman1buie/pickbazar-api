from django.db import models
from users.models import Artist


CATAGORY_TYPE = [
      ('CASUAL','Casual'),
      ('DRAWING','Deawing'),
      ('CAMERA_CLICK','Camera Click'),
      ('ART','Art'),
      ('OTHERS','Others'),
]


class PostImage(models.Model):
    descriptions = models.TextField(null=True, blank=True)
    image_title = models.CharField(max_length=200)
    catagory = models.CharField(max_length=50,choices=CATAGORY_TYPE, default='CAMERA_CLICK')
    uploaded_by = models.ForeignKey(to=Artist, on_delete=models.CASCADE, related_name='artists') 
    image_url = models.URLField(unique=True, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self) -> str:
         return f'Image of {self.image_title} by {self.uploaded_by.user.username}'
    
      
      