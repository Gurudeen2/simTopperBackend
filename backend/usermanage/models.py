from django.db import models

# Create your models here.


class Users(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    mobilenumber = models.CharField(max_length=15, blank=False)
    token = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.user_id
