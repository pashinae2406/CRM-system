from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    """Админ панель услуг"""

    change_list_template: str = 'admin/services_changelist.html'
    list_display: tuple = "pk", "name", "description", "price"
    list_display_links: tuple = "pk", "name"
    ordering: tuple = "name"
    fieldsets: list = [
        (None, {
            "fields": ("name", "description", "price"),
        }),
    ]
