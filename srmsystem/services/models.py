from django.db import models


class Service(models.Model):
    """Модель услуги"""

    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
