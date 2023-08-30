from django.shortcuts import render
from rest_framework import generics, response
from rest_framework.views import APIView
from .models import Dataprice
from .serializer import DataPriceSerializer



class GetDataPrice(generics.ListAPIView):
    queryset = Dataprice.objects.all()
    serializer_class = DataPriceSerializer


class CreateDataPrice(generics.CreateAPIView):
    serializer_class = DataPriceSerializer
    queryset = Dataprice.objects.all()


class DeleteDataPrice(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DataPriceSerializer
    queryset = Dataprice.objects.all()


class UpdateDataPrice(APIView):
    def put(self, request, id):
        print("request", request.data)
        return response.Response({"message": "Record updated Successfully"}, status=200)
    # logic here
