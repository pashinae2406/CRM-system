from django.db import models
from leads.models import Leads
# from contracts.models import Contracts
from ads.models import Ads


class Customers(models.Model):
    """Модель активного клиента"""

    lead = models.OneToOneField(Leads, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
