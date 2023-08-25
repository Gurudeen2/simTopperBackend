from rest_framework import serializers
from .models import NetworkProvider

class NetworkProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkProvider
        fields = ["providerID", "providerName"]