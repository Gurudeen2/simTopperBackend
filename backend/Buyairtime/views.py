from django.shortcuts import render
# import requests
from rest_framework.views import APIView
from rest_framework.response import Response

import json
# Create your views here.


# def buyairtime():
#     url = "https://www.arrifqubundle.com/api/topup/"
#     payload = {"network": 1, "amount": 50, "mobile_number": 8063641230,
#                "Ported_number": True, "airtime_type": "VTU"}
# # k = json.dumps(payload, indent=4)
# #     print("payload", k)
#     headers = {
#         'Authorization': 'Token 4f81017a394ceaaf050456dc31425d7395121712',
#         'Content-Type': 'application/json'
#     }
#     response = requests.request(
#         "POST", url, headers=headers, data=json.dumps(payload))
#     print("airtime we", response.text)
#     return


# def CK():

#     payloadCK = {

#         "UserID": "CK10136160",
#         "APIKey": "Z0U5H6E1E407E4GOBFL268B463S6260KNU2CADW1U762774KP53UZW0J1GU4D8VE",
#         "Amount": 50,
#         "MobileNetwork": "01",
#         "MobileNumber": 8063641230,
#         "CallBackURL": "/"
#     }
#     base_url = f'https://www.nellobytesystems.com/APIAirtimeV1.asp'
#     airtime = requests.get(base_url, params=json.dumps(payloadCK))
#     print("airitme", airtime.text)
#     return  # Response({"ip": ip.content, "airtime": airtime.content})
#     # base_url = f'https://www.nellobytesystems.com/APIAirtimeV1.asp?UserID={0}&APIKey={1}&MobileNetwork={2}&Amount={3}&MobileNumber={4}&CallBackURL={5}'.format(UserID, APIKey, MobileNetwork, Amount, MobileNumber, CallBackURL)
#    #   base_url = f'https://www.nellobytesystems.com/APIAirtimeV1.asp?UserID={UserID}&APIKey={APIKey}&MobileNetwork={MobileNetwork}&Amount={Amount}&MobileNumber={MobileNumber}&CallBackURL={CallBackURL}'
#    #   base_url = f'https://www.nellobytesystems.com/APIWalletBalanceV1.asp?UserID={UserID}&APIKey={APIKey}'
#     # ip_url = f'https://www.nellobytesystems.com/APIServerIPV1.asp?UserID={UserID}&APIKey={APIKey}'
#     # ip = requests.get(ip_url)

#     # response = requests.request("GET","https://www.nellobytesystems.com/APIAirtimeV1.asp?", params=params)


class BuyAirtime(APIView):

    def post(self, request):

        print("data", request.data["amount"])
        # amount = request.data["amount"]
        # mobileNumber = request.data["mobile_number"]
        # amount = request.data["amount"]
        # network = request.data["network"]

        # url = "https://www.arrifqubundle.com/api/topup/"
        # payload = {"network": network, "amount": amount, "mobile_number": mobileNumber,
        #            "Ported_number": True, "airtime_type": "VTU"}

        # headers = {
        #     'Authorization': 'Token 4f81017a394ceaaf050456dc31425d7395121712',
        #     'Content-Type': 'application/json'
        # }
        # response = requests.request(
        #     "POST", url, headers=headers, data=json.dumps(payload))
        # if response.status_code == 200:
        #     airtime = json.loads(response.content)
        # else:
        #     airtime = json.loads(response.content)

        return Response("airtime")
