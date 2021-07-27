from django.db import models

# Create your models here.

class DestinationType(models.Model):
	ABILITY_CHOICES = (
		(0,'Unrated'),
		(1,'Level One'),
		(2,'Level Two'),
		(3,'Level Three'),
		(4,'Level Four'),
		(5,'Level Five'),
		)

	name = models.CharField(max_length=200) # e.g Hospital, Clinic, Covid Vaccination Center etc.
	ability = models.PositiveIntegerField(choices=ABILITY_CHOICES, default=0, help_text='e.g Hospital = 5, Pharmacy = 1') # e.g Hospital = 5, Pharmacy = 1.

	def __str__(self):
		return self.name

class Destination(models.Model):
	RATING_CHOICES = (
		(0,'Unrated'),
		(1,'1 Star'),
		(2,'2 Stars'),
		(3,'3 Stars'),
		(4,'4 Stars'),
		(5,'5 Stars'),
		)	
	name = models.CharField(max_length=200, help_text='Location name e.g General Hospital, Kubwa') # field that holds actual hospital name e.g General Hospital, Kubwa
	rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
	latitude = models.FloatField()
	longitude = models.FloatField()
	destination_type = models.ForeignKey(DestinationType, on_delete=models.CASCADE)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Ride(models.Model):
	destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
	distance = models.PositiveIntegerField()

	def __str__(self):
		return self.destination