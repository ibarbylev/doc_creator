from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from docs.models import Doc


# @method_decorator(login_required, name='dispatch')
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


class DocsDetailsIndex(DetailView):
    model = Doc
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Details page'
        doc = context['doc']
        context['heading_text'] = f'Details of {doc.doc_name}'
        context['description'] = ''
        return context


class DocsCreateView(CreateView):
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


class DocsUpdateView(UpdateView):
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


class DocsDeleteView(DeleteView):
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
