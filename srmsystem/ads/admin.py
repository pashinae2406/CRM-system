from django.contrib import admin
from .models import Ads, PromotionChannel


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    """Админ панель рекламных кампаний"""

    change_list_template: str = 'admin/ads_changelist.html'
    list_display: tuple = 'pk', 'name', 'promotion_channel', 'budget'
    list_display_links: tuple = 'pk', 'name'
    ordering: tuple = "name"
    fieldsets: list = [
        (None, {
            "fields": ("name", "product", "promotion_channel", "budget"),
        })
    ]


@admin.register(PromotionChannel)
class PromotionChannelAdmin(admin.ModelAdmin):
    """Админ панель канала продвижения"""

    change_list_template: str = 'admin/channel_changelist.html'
    list_display: tuple = 'pk', 'name'
    list_display_links: tuple = 'pk', 'name'
    ordering: tuple = "name"
    fieldsets: list = [
        (None, {
            "fields": ("name",),
        })
    ]
