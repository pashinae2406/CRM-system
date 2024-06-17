from django.contrib import admin
from .models import Role, Employee


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    change_list_template = 'admin/role_changelist.html'
    list_display = 'pk', 'role', 'description'
    list_display_links = 'pk', 'role'
    ordering = 'pk', 'role',
    fieldsets = [
        (None, {
            "fields": ('role', 'description'),
        })
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    change_list_template = 'admin/role_changelist.html'
    list_display = 'pk', 'username', 'name', 'role'
    list_display_links = 'pk', 'name'
    ordering = 'pk', 'name',
    fieldsets = [
        (None, {
            "fields": ('user', 'username', 'password', 'name', 'role'),
        })
    ]
