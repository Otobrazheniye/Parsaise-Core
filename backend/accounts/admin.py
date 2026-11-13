from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "email", "full_name",
        "company", "status",
        "is_staff",)

    list_filter = (
        "status", "is_staff",
        "is_superuser", "is_active", )

    search_filter = (
        "email", "full_name",
        "company",)

    ordering = ("email",)

    read_only_fields = (
        "status", "created_at", 
        "last_login",)


    fieldsets = (
        (None, {
            "fields": ("email", "password"),
        }),
        ("Personal information", {
            "fields": (
                "full_name", "company",
                "status", ),
        }),
        ("Permissions", {
            "fields": (
                "is_active", "is_staff",
                "is_superuser",
                "groups", "user_permissions",),
        }),
        ("Important dates", {
            "fields": (
                "last_login", "created_at",),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "usable_password",
                "password1", "password2", ),
        }),
    )
