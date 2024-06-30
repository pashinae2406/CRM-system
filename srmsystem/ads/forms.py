from django import forms
from .models import Ads


class AdsForm(forms.ModelForm):

    """Форма создания/редактирования рекламной кампании"""

    class Meta:
        model = Ads
        fields: tuple = 'name', 'product', 'promotion_channel', 'budget'
        labels: dict = {
            'name': 'Название рекламной кампании',
            'product': 'Услуга',
            'promotion_channel': 'Канал продвижения',
            'budget': 'Бюджет'
        }
