from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from docs.models import Doc


class DocsListIndex(ListView):
    model = Doc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        context['heading_text'] = 'List of Documents'
        context['description'] = '''
        Select a document template to insert the data of your contractors. Or
        change the parameters of the document itself (But this option is only available for the administrator).
        '''
        return context


@method_decorator(login_required, name='dispatch')
class DocsDetailsIndex(UserPassesTestMixin, DetailView):
    model = Doc
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Details page'
        doc = context['doc']
        context['heading_text'] = f'Details of {doc.doc_name}'
        context['description'] = ''
        return context

    def test_func(self):
        # return self.request.user.is_superuser or self.request.user.is_staff
        return True


@method_decorator(login_required, name='dispatch')
class DocsDetailsForUsersIndex(UserPassesTestMixin, DetailView):
    model = Doc
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Details page'
        doc = context['doc']
        context['heading_text'] = f'Details of {doc.doc_name}'
        context['description'] = ''
        return context

    def test_func(self):
        # return self.request.user.is_superuser or self.request.user.is_staff
        return True


@method_decorator(login_required, name='dispatch')
class DocsCreateView(UserPassesTestMixin, CreateView):
    model = Doc
    fields = '__all__'
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

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


@method_decorator(login_required, name='dispatch')
class DocsUpdateView(UserPassesTestMixin, UpdateView):
    model = Doc
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create page'
        doc = context['doc']
        context['heading_text'] = f'Creating of {doc.doc_name}'
        context['description'] = f'On this page you can update the document {doc.doc_name}.'
        return context

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


@method_decorator(login_required, name='dispatch')
class DocsDeleteView(UserPassesTestMixin, DeleteView):
    model = Doc
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create page'
        doc = context['doc']
        context['heading_text'] = f'Delete of {doc.doc_name}'
        context['description'] = f'On this page you can update the document {doc.doc_name}.' \
                                 f'This operation cannot be canceled, so please be careful!'
        return context

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


@method_decorator(login_required, name='dispatch')
class TemplatePurchaseRequest(DeleteView):
    model = Doc
    context_object_name = 'doc'
    template_name = 'docs/template_purchase_request.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Purchase request'
        doc = context['doc']
        context['heading_text'] = f'Purchase request for the template "{doc}"'
        # context['description'] = f'On this page you can update the document {doc.doc_name}.'
        return context

