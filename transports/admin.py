from django.contrib import admin
from .models import Supplies, Transport, TransportType
# Register your models here.

admin.site.register(Supplies)
admin.site.register(TransportType)
admin.site.register(Transport)