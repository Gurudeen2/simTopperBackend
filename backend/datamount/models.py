from django.db import models

# Create your models here.


class DataAmount (models.Model):
    amount = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self) -> str:
        return self.amount
