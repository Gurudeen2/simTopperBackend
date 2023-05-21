from django.urls import path
from .views import BuyAirtime

urlpatterns=[
path("", BuyAirtime.as_view()  )
]