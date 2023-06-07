from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import hashlib
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib import auth
from datetime import datetime
import json


def ORD(data):
    charconv = 0
    for char in str(data):
        charconv += ord(char)
    return charconv


class CreateUser(APIView):

    def post(self, request):

        User = get_user_model()
        if request.method == "POST":
            email = request.data["email"]
            phoneno = request.data["phoneno"]
            fname = ORD(request.data["firstname"])
            password = request.data["password"]
            # try:
            # Users.objects.all().delete()

            if not User.objects.filter(email=email).exists():
                if not User.objects.filter(phone=phoneno).exists():
                    count = User.objects.all().count() + 1
                    userid = "TI" + str(fname) + str(count)
                    token = hashlib.sha3_256(
                        email.encode("UTF-8")).hexdigest()
                    # password = hashlib.sha3_256(
                    #     password.encode("UTF-8")).hexdigest()

                    users = User.objects.create_user(user_id=userid, first_name=request.data["firstname"],
                                                     last_name=request.data["lastname"], email=request.data["email"],
                                                     phone=phoneno, token=token, password=password)

                    users.save()

                    html = f""""
                                <html>
                                <head><title>
                                Registration Successful | TopIt
                                </title>
                                </head>
                                <body>
                                <p>
                                    Please invite others and enjoy swift transactions. Your details are below:
                                </p>
                                <p>
                                User ID: {userid}
                                    Email: {request.data["email"]} <br />
                                    Phone Number: {request.data["phoneno"]} <br />
                                    Password: {request.data["password"]}
                                </p>
                                </body>
                                </html>
                        """
                    # send email, phone and password
                    try:
                        send_mail(subject="Registration Successful", message="Thanks for registering",
                                  from_email="topit@admin.com", recipient_list=[request.data["email"]], html_message=html)
                    except Exception as err:
                        f = open("log.txt", "a")
                        f.write(
                            f"{datetime.now()} :: --> {err} --->, Module: usermanage \n")
                        f.close()
                    return Response("Registration Complete", status=200)
                else:
                    return Response("Phone Number Already Exist", status=403)
            else:
                return Response("Email Already Exist", status=403)
            # except Exception as e:
            #     message = e

        # return Response("message")


class LoginUser(APIView):
    def post(self, request):
        if request.method == "POST":
            username = request.data["phone"]
            password = request.data["password"]
            User = auth.authenticate(phone=username, password=password)
            print("User", User)
            if User is not None:
                user = get_user_model()

                user = user.objects.get(phone=username)
                userIt = auth.login(request, user)
                token = RefreshToken.for_user(user)

                return Response({"message": "Authentication Successful",
                                 "token": str(token)
                                 }, status=200)
            else:
                return Response("Authentication Failed", status=401)


class ChangePassword (APIView):
    def put(self, request):
        user = get_user_model()
        user = user.objects.get(phone=request.data["phone"])
        username = request.data["phone"]
        password = request.data["password"]
        if user.is_authenticated:

            user = user.objects.filter(
                phone=username).update(password=password)
            return Response({"message": "Password Successfully Changed"}, status=202)
        else:
            return Response({"message": "Account Doesn't Exist"}, status=404)


class Logout(APIView):
    def get(self, request):
        auth.logout(request)
        return Response(status=404)
