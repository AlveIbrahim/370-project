from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.car_listing)
admin.site.register(models.Car)
admin.site.register(models.Payment)

