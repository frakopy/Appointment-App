from django.db import models
from service.models import Service
from barber.models import Barber
from user.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_appointments')
    email = models.EmailField(verbose_name='customer email', max_length=254)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service_appointments")
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name="barber_appointments")
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=150, default="confirmed")
    comments = models.TextField(blank=True, null=True)
    event_id = models.CharField(max_length=250)
    event_url = models.URLField(max_length=500)


    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return self.event_url

