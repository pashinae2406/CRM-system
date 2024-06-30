from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):
    """Форма создания/редактированя услуги"""

    class Meta:
        model = Service
        fields: tuple = "name", "description", "price"
        labels: dict = {
            'name': 'Название',
            'description': 'Описание',
            'price': 'Стоимость'
        }
