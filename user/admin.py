from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):
    # Display specific columns to show in the panel
    list_display = ("first_name","last_name","email", "username", "phone")

    # Fields to be used in editing users
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {"fields": ["phone"]}),              
    )

    # Fields to be used when creating a user
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (    
        (None, {"fields": ["first_name", "last_name", "email", "phone"]}),
    )


admin.site.register(User, UserAdmin)
