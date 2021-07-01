from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100, blank=False)
    City = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    Country = models.CharField(max_length=50, blank=False)
    pincode = models.CharField(max_length=8, blank=False)
    mobile = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return f'{self.user.first_name}'


class Device(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.name


class IOTDevice(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="project_created_by")
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.device_name
