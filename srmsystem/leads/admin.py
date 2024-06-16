from django.contrib import admin
from .models import Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/leads_changelist.html'
    list_display = "pk", "last_name", "first_name",  "phone", "email", "ads"
    list_display_links = "pk", "last_name"
    ordering = "pk", "last_name",

    fieldsets = [
        (None, {
            "fields": ("last_name", "first_name",  "phone", "email", "ads"),
        }),
    ]
