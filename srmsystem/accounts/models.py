from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    advertising_company = models.CharField(max_length=50, blank=True, null=True)
