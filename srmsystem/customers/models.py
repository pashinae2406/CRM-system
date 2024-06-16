from django.db import models
from leads.models import Leads
from contracts.models import Contracts


class Customers(models.Model):
    lead = models.OneToOneField(Leads, on_delete=models.CASCADE, blank=True)
    contracts = models.ForeignKey(Contracts, on_delete=models.CASCADE, blank=True)
