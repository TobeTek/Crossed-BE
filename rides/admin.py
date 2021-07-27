from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.DestinationType)
admin.site.register(models.Destination)
admin.site.register(models.Ride)