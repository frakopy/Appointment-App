import datetime 

def get_availability(barber_events):
    hours = [
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
    ]

    busy_hours = []
    for time_object in barber_events:
        time_string = time_object[0].strftime("%H:%M")
        busy_hours.append(time_string)    
    available_hours = list(set(hours) - set(busy_hours))
    available_hours.sort()
    return available_hours
