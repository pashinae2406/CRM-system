from django import forms
from .models import Contracts


class ContractsForm(forms.ModelForm):
    """Форма создания/редактирования контракта"""

    class Meta:
        model = Contracts
        fields: tuple = 'customer', 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
        labels: dict = {
            'customer': 'Клиент',
            'name': 'Название контракта',
            'product': 'Предоставляемая услуга',
            'file': 'Файл с документом',
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
            'cost': 'Сумма'
        }
