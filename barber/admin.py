from django.contrib import admin
from .models import Barber


class BarberAdmin(admin.ModelAdmin):

    # Display specific columns to show in the panel
    list_display = ("name", "last_name", "phone", "email")


admin.site.register(Barber, BarberAdmin)
