from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    """Админ панель активных клиентов"""

    change_list_template: str = 'admin/customers_changelist.html'
    list_display: tuple = 'pk', 'last_name', 'first_name', 'phone', 'email', 'ads'
    list_display_links: tuple = 'pk', 'last_name'
    ordering: tuple = 'pk', 'lead'
    fieldsets: list = [
        (None, {
            "fields": ('lead', 'last_name', 'first_name', 'phone', 'email', 'ads'),
        })
    ]
