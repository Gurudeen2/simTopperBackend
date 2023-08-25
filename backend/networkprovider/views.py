from django.shortcuts import render
from .models import NetworkProvider
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.decorators import api_view
from django.core import serializers
from .serializer import NetworkProviderSerializer
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


class AllNetwork(generics.ListAPIView):
    # def get(self, request):
    queryset = NetworkProvider.objects.all()
    # network = serializers.serialize("json", NetworkProvider.objects.all())
    # network = json.loads(network)

    serializer_class = NetworkProviderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # return Response(network, status=200)


class DeleteNetwork(APIView):
    def delete(self, request, id):

        # providerID = request.data["providerID"]
        delete_network = NetworkProvider.objects.filter(providerID=id)
        delete_network.delete()
        # NetworkProvider.objects.delete(providerID=id)

        return Response({"message": "Successfully Deleted"}, status=200)
