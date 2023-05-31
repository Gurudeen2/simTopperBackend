from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.CharField(max_length=10, primary_key=True)
    phonenumber = models.CharField(max_length=20, blank=False)
    fname = models.CharField(max_length=50, blank=False)
    sname = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=True)
    token = models.CharField(max_length=100, blank=False, null=False)

