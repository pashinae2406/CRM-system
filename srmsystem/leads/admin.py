from django.contrib import admin
from .models import Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    """Админ панель потенциального клиента"""

    change_list_template: str = 'admin/leads_changelist.html'
    list_display: tuple = "pk", "last_name", "first_name",  "phone", "email", "ads"
    list_display_links: tuple = "pk", "last_name"
    ordering: tuple = "pk", "last_name",

    fieldsets: list = [
        (None, {
            "fields": ("last_name", "first_name",  "phone", "email", "ads"),
        }),
    ]
