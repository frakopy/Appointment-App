from django.template.loader import render_to_string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import environ, os, sys
# Add the upper dir to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.settings import BASE_DIR


def send_to_customer(dest_email, message):
    # Take environment variables from .env file
    env = environ.Env()
    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

    msg = MIMEMultipart("mixed")

    msg["From"] = env('EMAIL_HOST_USER')
    msg["To"] = dest_email
    msg["Subject"] = "Appointment confirmed"

    msg.attach(MIMEText(message, "html"))

    server = smtplib.SMTP(env('EMAIL_HOST'), 587)
    server.starttls()
    server.login(msg["From"], env('EMAIL_HOST_PASSWORD'))
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()

if __name__ == "__main__":
    send_to_customer("frako789@gmail.com", "Test from Django")
