from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.car_listing)
admin.site.register(models.Payment)
admin.site.register(models.share)
admin.site.register(models.Contact)
admin.site.register(models.Notification)
admin.site.register(models.cs_driver_ifo)

