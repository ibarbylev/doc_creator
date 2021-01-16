from django import forms

from production.models import DocumentsJournal


class CustomerForm(forms.ModelForm):
    pass


class DocumentsJournalForm(forms.ModelForm):
    class Meta:
        model = DocumentsJournal
        fields = '__all__'
