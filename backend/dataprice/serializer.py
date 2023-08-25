from rest_framework import serializers
from .models import Dataprice


class DataPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataprice
        fields = ['network', 'amount', 'duration', 'price']
