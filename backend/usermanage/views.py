from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
import hashlib
from django.core.mail import send_mail


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
            count = Users.objects.all().count() + 1

            if not Users.objects.filter(email=email).exists():
                if not Users.objects.filter(mobilenumber=phoneno).exists():
                    count = Users.objects.all().count() + 1
                    userid = "TI" + str(fname) + str(count)
                    token = hashlib.sha3_256(email.encode("UTF-8")).hexdigest()

                    users = Users.objects.create(user_id=userid, fname=request.data["firstname"],
                                                 sname=request.data["lastname"], email=request.data["email"],
                                                 mobilenumber=phoneno, token=token, password=request.data["password"])

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
                    send_mail(subject="Registration Successful", message="Thanks for registering",
                              from_email="akeemtolani2@gmail.com", recipient_list=[request.data["email"]], html_message=html)

                    message = "Registration Complete"
                else:
                    message = "Phone Number Already Exist!!!"
            else:
                message = "Email Already Exist!!!"
        return Response(message)
