from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    change_list_template = 'admin/customers_changelist.html'
    list_display = 'pk', 'last_name', 'first_name', 'phone', 'email', 'ads'
    list_display_links = 'pk', 'last_name'
    ordering = 'pk', 'lead',
    fieldsets = [
        (None, {
            "fields": ('lead', 'contracts', 'last_name', 'first_name', 'phone', 'email', 'ads'),
        })
    ]
