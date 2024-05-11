from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=256, blank=True, null=True)
    speciality = models.CharField(max_length=256, blank=True, null=True)
    profile_description = models.TextField(blank=True, null=True)
    rating = models.IntegerField()
    online_status = models.BooleanField()
    last_activity = models.DateTimeField(auto_now=True)
    image_url = models.URLField(blank=True, null=True)


class Client(models.Model):
    online_status = models.BooleanField()
    confirmation_of_payment = models.BooleanField(default=False)
    full_name = models.CharField(max_length=256)
    image_url = models.URLField(blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)
