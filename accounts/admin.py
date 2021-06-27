from django.contrib import admin

# Register your models here.
from accounts.models import Profile, IOTDevice

admin.site.register(Profile)
admin.site.register(IOTDevice)
