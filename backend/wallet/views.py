from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from .models import Wallet



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
        try:
            wallet = Wallet.objects.get(userId=userId)
        except Wallet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(WalletSerializer(wallet).data)

    def put(self, request, userId):

        wallet = Wallet.objects.get(userId=userId)
        serializer = WalletSerializer(wallet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GetWallet(APIView):
    def get(self, request, userId, format=None):
        wallet = Wallet.objects.get(userId=userId)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
