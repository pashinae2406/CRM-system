from django import forms
from .models import Leads


class LeadsForm(forms.ModelForm):
    """Форма создания/редактирования потенциального клиента"""

    class Meta:
        model = Leads
        fields: tuple = "first_name", "last_name", "phone", "email", "ads"
        labels: dict = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'email': 'Емейл',
            'ads': 'Рекламная кампания'
        }
