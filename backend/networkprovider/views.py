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
        for i in NetworkProvider.objects.all():
            print("mode", i.providerID)
        network = serializers.serialize("json", NetworkProvider.objects.all())
        net = json.loads(network)
        print("net", net)
        print("Dumps", json.dumps(net))
        return Response(network, status=200)


class DeleteNetwork(APIView):
    def post(self, request):
        return Response({"message": "Successfully Deleted"}, status=200)
