from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
import hashlib
from django.core.mail import send_mail

# Create your views here.


def ORD(data):
    charconv = 0
    for char in str(data):
        charconv += ord(char)
        print("char", char)
    return charconv


class CreateUser(APIView):

    def post(self, request):

        if request.method == "POST":
            email = request.data["email"]
            phoneno = request.data["phoneno"]
            fname = ORD(request.data["firstname"])

            print("firstname", fname)

            if not Users.objects.filter(email=email).exists():
                if not Users.objects.filter(mobilenumber=phoneno).exists():
                    count = Users.objects.all().count() + 1
                    print("count", count)
                    userid = "TI" + str(fname) + str(count)
                    token = hashlib.sha3_256(email.encode("UTF-8")).hexdigest()

                    users = Users.objects.create(user_id=userid, fname=request.data["firstname"],
                                                 sname=request.data["lastname"], email=request.data["email"],
                                                 mobilenumber=phoneno, token=token, password=request.data["password"])

                    # users.save()
                    print("token", token)
                    print("userid", userid)
                    html = f""""
                            <html>
                            <head><title>
                            Registration Successful | TopIt
                            </title>
                            </head>
                            <body>
                            <p>
                                Thanks for registering, please invite others and enjoy swift transactions.
                                  Your details are below:
                            </p>
                            <p>
                                Email: {request.data["email"]} <br />
                                Phone Number: {request.data["phoneno"]} <br />
                                Password: {request.data["password"]}
                            </p>
                            </body>
                            </html>
                    """
                    # send email, phone and password
                    send_mail(subject="Registration Successful", message=html,
                              from_email="akeemtolani2@gmail.com", recipient_list="akeemtolanifatai@gmail.com")

                    message = "Registration Complete"
                else:
                    message = "Phone Number Already Exist!!!"
            else:
                message = "Email Already Exist!!!"
        return Response("message")
