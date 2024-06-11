from django.urls import path
from .views import AppointmentView, AvailabilityView, AppointmentListView, update_event, delete_event

urlpatterns = [
    path("set_appointment/", AppointmentView.as_view(), name="set_appointment"),
    path("appointments/", AppointmentListView.as_view(), name="appointments"),
    path("availability/", AvailabilityView.as_view(), name="availability"),
    path("update_event/", update_event, name="update_event"),
    path("delete_event/<int:pk>/<str:eid>", delete_event, name="delete_event"),
]
