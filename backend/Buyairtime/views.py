from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import urllib.parse
import json
# Create your views here.


def buyairtime():
    url = "https://www.arrifqubundle.com/api/topup/"
    payload = "{\"network\": 1,\r\n \"amount\":50, \r\n \"mobile_number\": 08063641230,\r\n \"Ported_number\":true,\r\n \"airtime_type\":\"VTU\"}"
    k = json.loads(payload)
    print("payload", k)
    # headers = {
    #     'Authorization': 'Token 4f81017a394ceaaf050456dc31425d7395121712',
    #     'Content-Type': 'application/json'
    # }
    # response = requests.request("POST", url, headers=headers, data=payload)
    # print("airtime we", response.text)
    return


class BuyAirtime(APIView):
    def get(self, request):
        apikey = "JOBY94XGC4E8345NB27845W03TU0M3IFG6D0IFY923U118CDENU854SS361OG8A9"
        userId = "CK10136160"

        buyairtime()

        UserID = urllib.parse.quote("CK10136160")
        APIKey = urllib.parse.quote(
            "Z0U5H6E1E407E4GOBFL268B463S6260KNU2CADW1U762774KP53UZW0J1GU4D8VE")
      #   MobileNetwork = urllib.parse.quote("01")
        Amount = urllib.parse.quote("50")
        MobileNumber = urllib.parse.quote("08063641230")
        CallBackURL = urllib.parse.quote("www.arrifqubundle.com")
# https://www.arrifqubundle.com
        # UserID="CK10136160"
        # APIKey= "Z0U5H6E1E407E4GOBFL268B463S6260KNU2CADW1U762774KP53UZW0J1GU4D8VE"
        MobileNetwork = "01"
        # Amount="50"
        # MobileNumber="08063641230"
        # CallBackURL="/"

        # base_url = f'https://www.nellobytesystems.com/APIAirtimeV1.asp?UserID={0}&APIKey={1}&MobileNetwork={2}&Amount={3}&MobileNumber={4}&CallBackURL={5}'.format(UserID, APIKey, MobileNetwork, Amount, MobileNumber, CallBackURL)
        base_url = f'https://www.nellobytesystems.com/APIAirtimeV1.asp?UserID={UserID}&APIKey={APIKey}&MobileNetwork={MobileNetwork}&Amount={Amount}&MobileNumber={MobileNumber}&CallBackURL={CallBackURL}'
      #   base_url = f'https://www.nellobytesystems.com/APIAirtimeV1.asp?UserID={UserID}&APIKey={APIKey}&MobileNetwork={MobileNetwork}&Amount={Amount}&MobileNumber={MobileNumber}&CallBackURL={CallBackURL}'
      #   base_url = f'https://www.nellobytesystems.com/APIWalletBalanceV1.asp?UserID={UserID}&APIKey={APIKey}'
        ip_url = f'https://www.nellobytesystems.com/APIServerIPV1.asp?UserID={UserID}&APIKey={APIKey}'
        airtime = requests.get(base_url)
        ip = requests.get(ip_url)

        # print("airitme", airtime.text)
        # response = requests.request("GET","https://www.nellobytesystems.com/APIAirtimeV1.asp?", params=params)
        return Response({"ip": ip.content, "airtime": airtime.content})

    # def post(self, request):
    #    url = "https://www.arrifqubundle.com/api/user/"
    #    payload =  {"network": 1,
    #       "amount" :50,
    #       "mobile_number": "08063641230",
    #       "Ported_number":True,
    #       "airtime_type":"VTU"}
    #    headers = {
    #    'Authorization': 'Token 4f81017a394ceaaf050456dc31425d7395121712',
    #    'Content-Type': 'application/json'
    #    }

    #    response = requests.request("POST", url, headers=headers, data=payload)
    #    return Response(response.text)
