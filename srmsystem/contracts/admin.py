from django.contrib import admin
from .models import Contracts


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    """Админ панель контрактов"""

    change_list_template: str = "admin/contracts_changelist.html"
    list_display: tuple = 'pk', 'customer', 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
    list_display_links: tuple = 'pk', 'name'
    ordering: tuple = 'pk', 'name',
    fieldsets: list = [
        (None, {
            "fields": ('name', 'customer', 'file', 'product', 'start_date', 'end_date', 'cost'),
        })
    ]
