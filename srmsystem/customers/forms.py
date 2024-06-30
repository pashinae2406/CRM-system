from django import forms
from .models import Customers


class CustomerCreateForm(forms.ModelForm):
    """Форма создания активного клиента"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lead'].empty_label = 'Лид не выбран'

    class Meta:
        model = Customers
        fields: list = ['lead']
        labels: dict = {
            'lead': 'Лид',
        }


class CustomerTransferForm(forms.ModelForm):
    """Форма перевода потенциального клиента в активного"""

    class Meta:
        model = Customers
        fields: list = ['lead',]
        labels: dict = {
            'lead': 'Лид',
        }
