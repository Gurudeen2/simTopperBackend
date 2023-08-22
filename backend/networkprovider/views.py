from django.shortcuts import render
from .models import NetworkProvider
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
import json


class AddNetwork(APIView):
    def post(self, request):
        providerID = request.data["providerID"]
        providerName = request.data["providerName"]
        if NetworkProvider.objects.filter(providerID=providerID).exists():
            return Response({"message": "Already Exist"}, status=403)
        else:

            addnetwork = NetworkProvider.objects.create(
                providerID=providerID, providerName=providerName)
            addnetwork.save()
            return Response({"message": "Successfully Added"}, status=200)


class AllNetwork(APIView):
    def get(self, request):
        network = serializers.serialize("json", NetworkProvider.objects.all())
        network = json.loads(network)

        return Response(network, status=200)


class DeleteNetwork(APIView):
    def delete(self, request):
        print("provide", request.data)
        # providerID = request.data["providerID"]
        # NetworkProvider.objects.delete(providerID=providerID)

        return Response({"message": "Successfully Deleted"}, status=200)
