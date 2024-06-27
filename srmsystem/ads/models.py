from django.db import models
from services.models import Service


class Ads(models.Model):
    """Модель рекламной компании"""

    name = models.CharField(max_length=50, blank=True)
    product = models.ForeignKey(Service, on_delete=models.CASCADE)
    promotion_channel = models.TextField(max_length=50, blank=True, null=True)
    budget = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    leads_count = models.IntegerField(blank=True, null=True)
    customers_count = models.IntegerField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name
