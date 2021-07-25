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