from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    # Display specific columns to show in the panel
    list_display = (
        "email",
        "user",
        "service",
        "barber",
        "date",
        "time",
        "status",
        "comments",
        "event_url",
        "event_id",
    )


admin.site.register(Appointment, AppointmentAdmin)
