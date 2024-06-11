from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):

    # Display specific columns to show in the panel
    list_display = ("name", "price", "description")


admin.site.register(Service, ServiceAdmin)
