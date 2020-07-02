from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import BankBranch
from .serializer import BankBranchSerializer
from rest_framework import permissions


class ListBankDetailsView(generics.ListAPIView):
    """ 
    GET bank/
    GET bank/?name=<name>&city=<city>/
    All the bank name, ifsc, address, city, district, state
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        bankbranch_objects = BankBranch.objects.all()
        if name != None and city != None:
            bankbranch_objects = bankbranch_objects.filter(bank_name=name).filter(city=city)

        return bankbranch_objects



class BankDetailsIfscView(generics.RetrieveAPIView):
    """
    GET bank/<ifsc>/
    Bank details, for given ifsc
    """
    serializer_class = BankBranchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BankBranch.objects.filter(ifsc=self.kwargs.get('pk'))

