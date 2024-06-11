from django.contrib import admin
from .models import PaymentRecord


class PaymentRecordAdmin(admin.ModelAdmin):

    # Display specific columns to show in the panel
    list_display = (
        "customer_name",
        "customer_last_name",
        "appointment",
        "user",
        "payment_method",
        "created_at",
    )

    readonly_fields = ("created_at",)


admin.site.register(PaymentRecord, PaymentRecordAdmin)
