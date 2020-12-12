from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from production.models import Сustomer


class CustomerList(ListView):
    model = Сustomer
    template_name = 'production/customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customer List'
        customers = context['object_list']
        # user = context['user.username']
        # object_list = [customer for customer in customers if customer == request.user.username]
        context['heading_text'] = 'Customer List'
        context['description'] = '''
                '''
        return context


@method_decorator(login_required, name='dispatch')
class CustomerCreate(CreateView):
    model = Сustomer
    exclude = ('owner', )
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Updating page'
        context['heading_text'] = f'Updating New Document'
        context['description'] = '''
        On this page you can create a new document. 
        Please do not forget to add the html-template for this document to the folder: templates/docs/
        '''
        return context

# class DocumentsJournalList(ListView):
#     pass
