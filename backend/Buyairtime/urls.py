from django.urls import path
from .views import BuyAirtime
from usermanage.views import CreateUser, LoginUser, ChangePassword, Logout
from networkprovider.views import AddNetwork, AllNetwork, DeleteNetwork
from dataprice.views import CreateDataPrice, GetDataPrice

urlpatterns = [
    path("airtime/", BuyAirtime.as_view()),
    path("createuser/", CreateUser.as_view()),
    path("loginuser/", LoginUser.as_view()),
    path("changepassword/", ChangePassword.as_view()),
    path("logout/", Logout.as_view()),
    path("addnetwork/", AddNetwork.as_view()),
    path("getnetwork/", AllNetwork.as_view()),
    path("deletenetwork/<int:id>", DeleteNetwork.as_view()),
    path("getdataprice/", GetDataPrice.as_view()),
    path("adddataprice/", CreateDataPrice.as_view()),
]
