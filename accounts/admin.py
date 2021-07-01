from django.contrib import admin

# Register your models here.
from accounts.models import Profile, IOTDevice, Device

admin.site.register(Profile)
admin.site.register(IOTDevice)
admin.site.register(Device)
