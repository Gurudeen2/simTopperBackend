from django.db import models
from networkprovider.models import NetworkProvider

# Create your models here.


class Dataprice(models.Model):
    network = models.ForeignKey(
        NetworkProvider, on_delete=models.CASCADE, null=False, blank=False)
    amount = models.CharField(max_length=10, blank=False, null=False)
    duration = models.CharField(max_length=10, blank=False, null=False)
    price = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.network.providerName
