from django.shortcuts import render
from django.views.generic import ListView, DetailView

from docs.models import Doc


class DocsListIndex(ListView):
    model = Doc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        context['heading_text'] = 'List of Documents'
        context['description'] = '''
        Select a document template to insert the data of your contractors.
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

