from django.db import models


class NetworkProvider(models.Model):
    providerID = models.IntegerField(unique=True)
    providerName = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.providerName
