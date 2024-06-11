from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["email", "service", "barber", "date", "time","comments"]
        exclude = ("user", "status", "event_url", "event_id")
        widgets = {
            "date": forms.DateInput(
                attrs={"type": "date", "class": "form-control", "disabled": True}
            ),
            "time": forms.Select(choices=[], attrs={"disabled": True}),
            "comments": forms.Textarea(attrs={"rows": 5}),
        }
