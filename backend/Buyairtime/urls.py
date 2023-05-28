from django.urls import path
from .views import BuyAirtime
from usermanage.views import CreateUser, LoginUser

urlpatterns = [
    path("airtime/", BuyAirtime.as_view()),
    path("createuser/", CreateUser.as_view()),
    path("loginuser/", LoginUser.as_view()),
]
