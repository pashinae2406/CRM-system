from django.contrib import admin
from .models import Contracts


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    change_list_template = "admin/contracts_changelist.html"
    list_display = 'pk', 'name', 'product', 'file', 'start_date', 'end_date', 'cost'
    list_display_links = 'pk', 'name'
    ordering = 'pk', 'name',
    fieldsets = [
        (None, {
            "fields": ('name', 'file', 'product', 'start_date', 'end_date', 'cost'),
        })
    ]
