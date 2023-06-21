from django.urls import path
from .views import BuyAirtime
from usermanage.views import CreateUser, LoginUser, ChangePassword, Logout
from networkprovider.views import AddNetwork, AllNetwork, DeleteNetwork

urlpatterns = [
    path("airtime/", BuyAirtime.as_view()),
    path("createuser/", CreateUser.as_view()),
    path("loginuser/", LoginUser.as_view()),
    path("changepassword/", ChangePassword.as_view()),
    path("logout/", Logout.as_view()),
    path("addnetwork/", AddNetwork.as_view()),
    path("getnetwork/", AllNetwork.as_view()),
    path("deletenetwork/", DeleteNetwork.as_view()),
]
