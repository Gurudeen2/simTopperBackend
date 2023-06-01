
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
import hashlib
from django.core.mail import send_mail
from datetime import datetime


def ORD(data):
    charconv = 0
    for char in str(data):
        charconv += ord(char)
    return charconv


class CreateUser(APIView):

    def post(self, request):

        if request.method == "POST":
            email = request.data["email"]
            phoneno = request.data["phoneno"]
            fname = ORD(request.data["firstname"])
            password = request.data["password"]

            # try:
            # Users.objects.all().delete()

            if not Users.objects.filter(email=email).exists():
                if not Users.objects.filter(mobilenumber=phoneno).exists():
                    count = Users.objects.all().count() + 1
                    userid = "TI" + str(fname) + str(count)
                    token = hashlib.sha3_256(
                        email.encode("UTF-8")).hexdigest()
                    password = hashlib.sha3_256(
                        password.encode("UTF-8")).hexdigest()

                    users = Users.objects.create(user_id=userid, fname=request.data["firstname"],
                                                 sname=request.data["lastname"], email=request.data["email"],
                                                 mobilenumber=phoneno, token=token, password=password)

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
                                  from_email="akeemtolani2@gmail.com", recipient_list=[request.data["email"]], html_message=html)
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

        # return Response(message)


class LoginUser(APIView):
    def post(self, request):
        if request.method == "POST":
            username = request.data["username"]
            password = request.data["password"]
            if Users.objects.filter(mobilenumber=username).exists() or Users.objects.filter(email=username).exists():
                password = hashlib.sha3_256(
                    password.encode("UTF-8")).hexdigest()
                if Users.objects.filter(password=password).exists():
                    # user = Users.objects.filter(
                    #     mobilenumber=username).first() or Users.objects.filter(email=username).first()
                    # token, created = Token.objects.get_or_create(user=user.mobilenumber)

                    # print("users", user.mobilenumber)
                    # print("token", token)
                    return Response({"message": "Login Successful",
                                    #  "token": token
                                     }, status=200)
            else:
                return Response("Account Does Not Exist", status=401)
        # return Response(status=200)
