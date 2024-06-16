from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    change_list_template = 'admin/customers_changelist.html'
    list_display = 'pk', 'lead'
    list_display_links = 'pk', 'lead'
    ordering = 'pk', 'lead',
    fieldsets = [
        (None, {
            "fields": ('lead', 'contracts'),
        })
    ]
