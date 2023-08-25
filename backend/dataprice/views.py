from django.shortcuts import render
from rest_framework import generics
from .models import Dataprice
from .serializer import DataPriceSerializer

# Create your views here.


class GetDataPrice(generics.ListCreateAPIView):
    queryset = Dataprice.objects.all()
    serializer_class = DataPriceSerializer

class CreateDataPrice
