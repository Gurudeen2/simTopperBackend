from django.urls import path
from .views import BuyAirtime
from usermanage.views import CreateUser, LoginUser, ChangePassword, Logout
from networkprovider.views import AddNetwork, AllNetwork, DeleteNetwork
from dataprice.views import CreateDataPrice, GetDataPrice, DeleteDataPrice
from datamount.views import CreateDataAmount, DeleteDataAmount
from wallet.views import createWallet, GetWallet, updateWallet

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
    path("dataprice/<str:pk>", DeleteDataPrice.as_view()),
    path('dataamount/', CreateDataAmount.as_view()),
    path('dataamountchange/<int:pk>', DeleteDataAmount.as_view()),
    path('createwallet/', createWallet.as_view()),
    path('getwallet/<userId>', GetWallet.as_view()),
    path('updatewallet/<userId>', updateWallet.as_view())
]
