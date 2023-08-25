from django.shortcuts import render
from rest_framework import generics, response
from rest_framework.views import APIView
from .models import Dataprice
from .serializer import DataPriceSerializer

# Create your views here.


class GetDataPrice(generics.ListAPIView):
    queryset = Dataprice.objects.all()
    serializer_class = DataPriceSerializer


class CreateDataPrice(generics.CreateAPIView):
    serializer_class = DataPriceSerializer
    queryset = Dataprice.objects.all()

class DeleteDataPrice(generics.DestroyAPIView):
    # logic here


class UpdateDataPrice(generics.UpdateAPIView):
    #logic here
