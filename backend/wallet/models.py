from django.db import models
# from usermanage.models import Users
from datetime import datetime

# Create your models here.


class Wallet(models.Model):
    walletId = models.CharField(
        primary_key=True, max_length=10, blank=False, null=False)
    userId = models.CharField(max_length=20, blank=False, null=False)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date_fund = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.walletId
