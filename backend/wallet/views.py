from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers
from .models import Wallet


# Create your views here.

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class createWallet(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class createWall

class ListWallet(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class GetWallet(APIView):
    def get(self, request, walletId):
        wallet = Wallet.objects.get(walletId=walletId)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
