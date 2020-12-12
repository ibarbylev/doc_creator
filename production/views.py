from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from production.models import Сustomer


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
    fields = ['first_name', 'last_name', 'email']
    # fields = '__all__'
    template_name = 'production/customer_create.html'
    # exclude = ('owner', )
    success_url = reverse_lazy('customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Updating page'
        context['heading_text'] = f'Creating New Customer'
        context['description'] = ''
        return context

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.owner = self.request.user
        customer.save()  # This is redundant, see comments.
        return super(CustomerCreate, self).form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     pass
    #     customer = form.form.save(commit=False)
