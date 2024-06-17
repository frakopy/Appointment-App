from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json, environ, os, sys
# from .formatTime import get_start_end_time

# Add the upper dir to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.settings import BASE_DIR


# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

class GoogleCalendar:

    def __init__(self):
        self.credentials = env("GOOGLE_SERVICE_ACCOUNT_CREDENTIALS")
        self.credentials = json.loads(self.credentials)
        self.calendar_id = env("CALENDAR_ID")
        self.service = build(
            "calendar",
            "v3",
            credentials=service_account.Credentials.from_service_account_info(
                self.credentials, scopes=["https://www.googleapis.com/auth/calendar"]
            ),
        )

    def create_event(self, event_name, description ,s_time, e_time, t_zone):
        event = {
            "summary": event_name,
            "description": description,
            "start": {
                "dateTime": s_time,
                "timeZone": t_zone,
            },
            "end": {
                "dateTime": e_time,
                "timeZone": t_zone,
            },
        }

        try:
            created_event = self.service.events().insert(calendarId = self.calendar_id, body=event).execute()
        except HttpError as error:
            raise Exception("Ups! we got the error: ", error)

        return created_event

    def get_event_list(self):
        events_result = (
            self.service.events()
            .list(
                calendarId=self.calendar_id,
                timeMin="2024-06-08T00:00:00-05:00",
                timeMax=("2024-06-09T00:00:00-05:00"),
            )
            .execute()
        )
        return events_result

    def get_event(self):
        event = self.service.events().get(calendarId=self.calendar_id, eventId="oiv4bi42g9irg0ckh6er5h77k8").execute()
        return event

    def update_event(self, id, start_time, end_time, time_zone):
        # First retrieve the event from the API.
        event = self.service.events().get(calendarId=self.calendar_id,eventId=id).execute()

        #  Update the event
        event["start"] = {
            "dateTime": start_time,
            "timeZone": time_zone,
        }
        event["end"] = {
            "dateTime": end_time,
            "timeZone": time_zone,
        }

        updated_event = (
            self.service.events()
            .update(calendarId=self.calendar_id, eventId=event["id"], body=event)
            .execute()
        )

        return updated_event

    def delete_event(self, id):
        self.service.events().delete(calendarId=self.calendar_id, eventId=id).execute()

if __name__ == "__main__":
    #  Creating Google Calendar object
    google = GoogleCalendar()

    print("Google Calendar instance created: ", google)

    # Delete an event
    # google.delete_event("s1pfacoldi518nrj1fcq5rdrs0")

    # # Update an event
    # event_id = "1k9mc5c9bjv06scdq1nv0qpmh0"
    # date = "2024-06-09"
    # time = "17:00:00"
    # time_zone = "America/Chicago"
    # start_time, end_time = get_start_end_time(date, time)
    # event_updated = google.update_event(event_id, start_time, end_time, time_zone)
    # print(event_updated)

    # Create an event
    # event = google.create_event(
    #     "Appointment reservation successful",
    #     "Appointment reserved",
    #     "2024-05-30T11:00:00-05:00",
    #     "2024-05-30T12:15:00-05:00",
    #     "America/Chicago",
    # )
