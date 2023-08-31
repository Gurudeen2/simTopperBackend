from django.shortcuts import render
from rest_framework import generics, serializers
from .models import DataAmount

# Create your views here.


class DataAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAmount
        fields = '__all__'


class CreateDataAmount(generics.ListCreateAPIView):
    serializer_class = DataAmountSerializer
    queryset = DataAmount.objects.all()


class DeleteDataAmount(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataAmountSerializer
    queryset = DataAmount.objects.all()
