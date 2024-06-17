from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    """Модель роли сотрудника"""
    role = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.role


class Employee(models.Model):
    """Модель сотрудника"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
