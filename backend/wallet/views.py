from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers
from .models import Wallet
import json


# Create your views here.

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class UpdateWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["amount", "date_fund"]


class createWallet(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class updateWallet(APIView):
    def get(self, request, userId):
        wallet = Wallet.objects.get(userId=userId)
        return Response(WalletSerializer(wallet).data)

    def put(self, request, userId):

        # {'walletId': '4', 'userId': '1', 'amount': '10000.00',
        #     'date_fund': '2023-09-23T16:26:00Z'}
        wallet = Wallet.objects.filter(userId=userId)

        wallet.update(amount=request.data["amount"],
                      date_fund=request.data["date_fund"])
        serializer = UpdateWalletSerializer(wallet)
        return Response(serializer.data)


class ListWallet(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class GetWallet(APIView):
    def get(self, request, userId, format=None):
        wallet = Wallet.objects.get(userId=userId)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
