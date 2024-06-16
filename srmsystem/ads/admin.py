from django.contrib import admin
from .models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/ads_changelist.html'
    list_display = 'pk', 'name', 'promotion_channel', 'budget'
    list_display_links = 'pk', 'name'
    ordering = "name",
    fieldsets = [
        (None, {
            "fields": ("name", "product", "promotion_channel", "budget"),
        })
    ]

