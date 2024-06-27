from django.db import models
from services.models import Service
from customers.models import Customers


def file_contracts_directory_path(instance: "Contracts", filename: str) -> str:
    return f"files/file_contracts_{instance.pk}/{filename}"


class Contracts(models.Model):
    """Модель контракта"""

    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    product = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True)
    file = models.FileField(blank=True, null=True, upload_to=file_contracts_directory_path)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
