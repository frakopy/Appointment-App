from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from django.template.loader import render_to_string
from .threads import SendEmailThread 


@receiver(post_save, sender=Appointment)
def send_email(sender, instance, **kwargs):
    dest_email = instance.email
    customer_name = instance.user.first_name
    barber_name = instance.barber.name
    date = instance.date
    time = instance.time

    message = render_to_string(
        "appointment/notification.html",
        {"username": customer_name, "barber": barber_name, "date": date, "time": time},
    )

    # Instantiate the class SendEmailThread and invoke its run method Which will send the email
    SendEmailThread(dest_email, message).start()
