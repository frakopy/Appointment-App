import json
import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView
from utilities.googleCalendar import GoogleCalendar
from utilities.formatTime import get_start_end_time
from .forms import AppointmentForm
from .models import Appointment
from utilities.availability import get_availability
from django.contrib.auth.mixins import LoginRequiredMixin
from .threads import UpdateEventThread, DeleteEventThread


class AppointmentView(LoginRequiredMixin, CreateView):
    login_url = "login"
    template_name = "appointment/set_appointment.html"
    form_class = AppointmentForm

    def form_valid(self, form):
        # Getting form data for create google calendar event
        service = form.cleaned_data["service"]
        barber = form.cleaned_data["barber"]
        date = form.cleaned_data["date"]
        time = form.cleaned_data["time"]
        user = self.request.user
        start_time, end_time = get_start_end_time(date, time)

        # Create google calendar event
        google = GoogleCalendar()

        event = google.create_event(
            f"Appointment for: {service}",
            f"Reserved between {user.first_name} and the barber {barber}",
            f"{start_time}",
            f"{end_time}",
            "America/Chicago",
        )

        # Adding new fields and saving the appointment in the database
        form.instance.user = user
        form.instance.event_url = event["htmlLink"]
        form.instance.event_id = event["id"]
        form.save()

        # Adding a custom event (created) for HTMX 
        response = HttpResponse()
        response["HX-Trigger"] = "created"
        return response


class AvailabilityView(View):
    def post(self, request, *args, **kwargs):
        jsonPost = json.loads(request.body.decode("utf-8"))
        date = jsonPost["date"]
        barber_id = jsonPost["barberId"]
        barber_events = Appointment.objects.filter(
            barber_id=barber_id, date=date
        ).values_list("time")
        available_hours = get_availability(barber_events)
        return JsonResponse({"hours": available_hours, "result": "ok"})


class AppointmentListView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = Appointment
    template_name = "appointment/appointments.html"

    def get_queryset(self):
        queryset = Appointment.objects.filter(user=self.request.user)
        return queryset


def update_event(request):
    if request.method == "POST":
        date = request.POST.get("date")
        str_time = request.POST.get("time") + ":00"
        appointment_id = request.GET.get("id")
        event_id = request.GET.get("event-id")
        time = datetime.datetime.strptime(str_time, "%H:%M:%S").time()
        time_zone = "America/Chicago"
        if appointment_id and event_id and date and time:
            # Update google calendar event in background
            UpdateEventThread(event_id, date, time, time_zone).start()
            # Update the appointment from database
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.date = date
            appointment.time = time
            appointment.save()
        else:
            print("Some of following was not received: id | date | time")
            return HttpResponse("<div class='text-center mt-5'>Something was wrong, check console logs</div>")

    return redirect("appointments")

def delete_event(request, pk, eid):
    if request.method == "DELETE":
        try:
            # Delete google calendar event in background
            DeleteEventThread(eid).start()
            # Delete the appointment from database
            appointment = Appointment.objects.get(pk=pk)
            appointment.delete()
            appointment_list = Appointment.objects.all()
            context = {"appointment_list": appointment_list}
            response = render(request, "appointment/list_appointments.html", context)
            response["HX-Trigger"] = "deleted"
            return response
        except Exception as e:
            print("Error when trying to retrieve appointment object: " + str(e))
    else:
        return HttpResponse("<div class='text-center mt-5'>Bad Request</div>")
