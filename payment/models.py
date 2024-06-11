from django.db import models
from appointment.models import Appointment
from user.models import User


class PaymentRecord(models.Model):
    customer_name = models.CharField(max_length=250)
    customer_last_name = models.CharField(max_length=250)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'PaymentRecord'
        verbose_name_plural = 'PaymentRecords'

    def __str__(self):
        pass

