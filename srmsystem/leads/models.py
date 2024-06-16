from django.db import models
from ads.models import Ads


class Leads(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"