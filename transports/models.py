from django.db import models
# from accounts.models import Driver

# Create your models here.

class Supplies(models.Model):
	name = models.CharField(max_length=200, unique=True)
	desription = models.CharField(max_length=200, blank=True)
	application_method = models.TextField(blank=True)

class TransportType(models.Model):
	name = models.CharField(max_length=200, unique=True)

class Transport(models.Model):
	RATING_CHOICES = (
		(0,'Unrated'),
		(1,'1 Star'),
		(2,'2 Stars'),
		(3,'3 Stars'),
		(4,'4 Stars'),
		(5,'5 Stars'),
		)
	# driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='transport')
	supplies = models.ManyToManyField(Supplies, related_name='transports',null=True)
	rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
	transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE, related_name='transports')







