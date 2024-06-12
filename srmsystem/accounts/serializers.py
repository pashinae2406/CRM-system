from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Сериалайзер для регистрации пользователей"""

    model = Client
    fields = [
        'name',
        'phone',
        'email',
        'advertising_company'
    ]
