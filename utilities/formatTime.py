import pytz
from datetime import datetime, timedelta

def get_start_end_time(date, time):
    # Combine date and time into a single datetime object
    datetime_str = f"{date} {time}"
    naive_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

    # Set the timezone to America/Chicago
    chicago_tz = pytz.timezone("America/Chicago")
    localized_datetime = chicago_tz.localize(naive_datetime)

    # Format datetime to the required format for Google Calendar
    start_time = localized_datetime.isoformat()

    # Assuming the event lasts 1 hour, adjust as necessary
    end_time = (localized_datetime + timedelta(hours=1)).isoformat()

    return start_time, end_time

if __name__ == "__main__":
    start, end = get_start_end_time("2024-05-30", "10:00")

    print(start)
    print(end)
