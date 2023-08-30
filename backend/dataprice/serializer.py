from rest_framework import serializers
from .models import Dataprice


class DataPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataprice
        fields = '__all__'
