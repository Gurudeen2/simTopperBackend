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
    # print
    serializer_class = DataPriceSerializer
    queryset = Dataprice.objects.all()

class DeleteDataPrice(APIView):
    def delete(self, request, id):
        return response.Response({"message":"Record Deleted"})
    # logic here


class UpdateDataPrice(APIView):
    def put(self, request, id):
        print("request", request.data)
        return response.Response({"message":"Record updated Successfully"}, status=200)
    #logic here
