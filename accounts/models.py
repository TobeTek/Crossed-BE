from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

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