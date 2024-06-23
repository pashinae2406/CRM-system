from django import forms
from .models import Customers
from leads.models import Leads


class CustomerCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lead'].empty_label = 'Лид не выбран'
        self.fields['contracts'].empty_label = 'Контракт не выбран'

    class Meta:
        model = Customers
        fields = ['lead', 'contracts']
        labels = {
            'lead': 'Лид',
            'contracts': 'Контракты'
        }


class CustomerTransferForm(forms.ModelChoiceField):

    try:
        lead = forms.ModelChoiceField(label='Лид', queryset=Leads.objects.get(id=1))
    except:
        print()

    class Meta:
        model = Customers
        fields = ['lead', 'contracts']
        labels = {
            'lead': 'Лид',
            'contracts': 'Контракты'
        }
