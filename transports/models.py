from django.db import models
from django.contrib.auth import get_user_model



class Supplies(models.Model):
	name = models.CharField(max_length=200, unique=True)
	description = models.CharField(max_length=200, blank=True)
	application_method = models.TextField(blank=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'Supplies'


class TransportType(models.Model):
	name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.name


class Transport(models.Model):
	RATING_CHOICES = (
		(0,'Unrated'),
		(1,'1 Star'),
		(2,'2 Stars'),
		(3,'3 Stars'),
		(4,'4 Stars'),
		(5,'5 Stars'),
		)
	driver = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='transports')
	supplies = models.ManyToManyField(Supplies, related_name='transports', blank=True)
	rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
	transport_type = models.ForeignKey(TransportType, on_delete=models.CASCADE, related_name='transports')
	license_number = models.CharField(max_length=30)

	def __str__(self):
		return "{} Driver: {} {}".format(self.transport_type, self.driver.first_name, self.driver.last_name)





