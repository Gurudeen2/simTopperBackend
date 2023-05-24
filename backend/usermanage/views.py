from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import Users

# Create your views here.
#  = models.CharField(max_length=10, primary_key=True)
#     fullname = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, blank=True)
#     mobilenumber = models.CharField(max_length=15, blank=False)
#     token = models.CharField(max_length=100, blank=False, null=False)
#     password


class CreateUser(APIView):
    # {'firstname': 'Akeem', 'lastname': 'Fatai', 'email': 'akeemtolanifatai@gmail.com', 'password': 'tolani100', 'phoneno': '8970'}
    def post(self, request):
        print(request.data)
        # if request.method == "POST":
        # Users.objects.create(user_id=)
        return Response("status")
