from django.urls import path
from . import views
from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView


app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path('aboutus/',views.aboutus, name="aboutus"),
    path('userdata/', views.userdata, name="userdata")
]
