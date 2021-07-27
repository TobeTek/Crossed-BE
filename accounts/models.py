from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
THUMBNAIL_DIMENSIONS = (200,200) 

class CustomUser(AbstractUser):
    """
    Extra fields

    """
    USER_TYPE_CHOICES = (
            ('C', 'Customer'),
            ('D','Driver'),
            ('H', 'Hospital')
        ) 
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='C')
    profile_picture = models.ImageField(upload_to='profile-images/img/', null=True)
    thumbnail_picture = ResizedImageField(size=THUMBNAIL_DIMENSIONS, quality=100, upload_to='profile-images/thumbnails/', null=True, blank=True)        


class DriverProfile(models.Model):
    
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    RATING_CHOICES = (
        (0,'Unrated'),
        (1,'1 Star'),
        (2,'2 Stars'),
        (3,'3 Stars'),
        (4,'4 Stars'),
        (5,'5 Stars'),
        )
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    ip_address = models.CharField(max_length=9)
    working = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)