# start
from django.urls import path, re_path
from .views import ListBankDetailsView, BankDetailsIfscView

urlpatterns = [
    path('bank/<str:pk>/', BankDetailsIfscView.as_view(), name="bank-details"),
    re_path(r'^bank/$', ListBankDetailsView.as_view(), name="banks-all"),
    re_path(r'^bank$', ListBankDetailsView.as_view(), name="banks-all"),
]
