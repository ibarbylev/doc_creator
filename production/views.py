from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from production.forms import DocumentsJournalForm
from production.models import Сustomer, AvailableDocs, DocumentsJournal


@method_decorator(login_required, name='dispatch')
class CustomerList(ListView):
    model = Сustomer
    template_name = 'production/customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customer List'
        # customers = context['object_list']
        # user = context['user.username']
        # object_list = [customer for customer in customers if customer == request.user.username]
        context['heading_text'] = 'Customer List'
        context['description'] = '''
                '''
        return context


# @method_decorator(login_required, name='dispatch')
class CustomerCreate(CreateView):
    model = Сustomer
    # fields = ['first_name', 'last_name', 'email']
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Updating page'
        context['heading_text'] = f'Creating New Customer'
        context['description'] = ''
        return context

    def form_valid(self, form):
        сustomer = form.save(commit=False)
        сustomer.owner = self.request.user
        сustomer.save()  # This is redundant, see comments.
        return super(CustomerCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CustomerUpdate(UpdateView):
    model = Сustomer
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Updating page'
        сustomer = context['сustomer']
        context['heading_text'] = f'Updating Customer {сustomer}'
        context['description'] = f''
        return context


@method_decorator(login_required, name='dispatch')
class CustomerDelete(DeleteView):
    model = Сustomer
    success_url = reverse_lazy('customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Deleting page'
        сustomer = context['сustomer']
        context['heading_text'] = f'Deleting Customer {сustomer}'
        return context

# Views for users' own documents ====================================


@method_decorator(login_required, name='dispatch')
class UsersDocsList(ListView):
    model = AvailableDocs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List of Available Docs'
        context['heading_text'] = f'List of Available Docs'
        return context


@method_decorator(login_required, name='dispatch')
class UsersDocsDelete(DeleteView):
    model = AvailableDocs
    success_url = reverse_lazy('users_docs_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Deleting page'
        availabledocs = context['availabledocs']
        context['heading_text'] = f'Deleting Customer {availabledocs}'
        return context


@method_decorator(login_required, name='dispatch')
class UsersDocsFill(ListView):
    model = DocumentsJournal
    success_url = reverse_lazy('users_docs_not_filing_fields')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Docs'
        context['form'] = DocumentsJournalForm()
        context['heading_text'] = f'Choose DocName and Customer to fill out of document'
        return context

    # def post(self, request, pk, *args, **kwargs):
