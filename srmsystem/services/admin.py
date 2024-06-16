from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    change_list_template = 'admin/services_changelist.html'
    list_display = "pk", "name", "description", "price"
    list_display_links = "pk", "name"
    ordering = "name",
    fieldsets = [
        (None, {
            "fields": ("name", "description", "price"),
        }),
    ]
