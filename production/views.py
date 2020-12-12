from django.shortcuts import render
from django.views.generic import ListView

from production.models import Сustomer


class CustomerList(ListView):
    model = Сustomer
    template_name = 'production/customers.html'


# class DocumentsJournalList(ListView):
#     pass
