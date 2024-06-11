import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import environ, os
from core.settings import BASE_DIR
from utilities.googleCalendar import GoogleCalendar
from utilities.formatTime import get_start_end_time

class SendEmailThread(threading.Thread):

    def __init__(self, dest_email, message):
        # Take environment variables from .env file
        self.env = environ.Env()
        environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

        self.dest_email = dest_email
        self.message = message
        threading.Thread.__init__(self)

    def run(self):
        print("Trying to send email...")
        try:
            msg = MIMEMultipart("mixed")
            msg["From"] = self.env('EMAIL_HOST_USER')
            msg["To"] = self.dest_email
            msg["Subject"] = "Appointment confirmed"

            msg.attach(MIMEText(self.message, "html"))

            server = smtplib.SMTP(self.env('EMAIL_HOST'), 587)
            server.starttls()
            server.login(msg["From"], self.env('EMAIL_HOST_PASSWORD'))
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            server.quit()
            print("Email successfully sent")

        except Exception as e:
            print("Got following error when trying to send the email: " + str(e))


class UpdateEventThread(threading.Thread):

    def __init__(self, event_id, date, time, time_zone):
        self.event_id = event_id
        self.date = date
        self.time = time
        self.time_zone = time_zone
        self.google = GoogleCalendar()
        threading.Thread.__init__(self)

    def run(self):
        print("updating event")
        try:
            start_time, end_time = get_start_end_time(self.date, self.time)
            event_updated = self.google.update_event(self.event_id, start_time, end_time, self.time_zone)
            print("Event successfully updated")
        except Exception as e:
            print("Got following error when trying to update the event: " + str(e))


class DeleteEventThread(threading.Thread):

    def __init__(self, event_id):
        self.event_id = event_id
        self.google = GoogleCalendar()
        threading.Thread.__init__(self)

    def run(self):
        print("Deleting event")
        try:
            self.google.delete_event(self.event_id)
            print("Event successfully deleted")
        except Exception as e:
            print("Got following error when trying to update the event: " + str(e))
