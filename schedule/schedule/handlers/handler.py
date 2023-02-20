from datetime import datetime


schedule = {
    1: "06:00-08:00,14:00-16:00,22:00-00:00",
    2: "04:00-06:00,12:00-14:00,20:00-22:00",
    3: "02:00-04:00,10:00-12:00,18:00-20:00",
    4: "00:00-02:00,08:00-10:00,16:00-18:00",
}

WEEKDAYS = {
    "Friday": 1,
    "Sunday": 1,
    "Saturday": 1,
    "Mondauy": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
}


def schedule_in_string(day: str) -> str:
    # Split the string by commas
    new_day = "\n".join(day.split(","))
    # Join the string with new lines
    return new_day



def display_schedule(d: str):
    today = datetime.now().strftime("%d.%m")
    exactly_day = datetime.now().strftime("%A")
    return f"Schedule for {today} - {exactly_day}: \n{d}"


def check_schedule_day():
    exactly_day = datetime.now().strftime("%A")
    day_schedule = schedule[WEEKDAYS[exactly_day]]
    return display_schedule(schedule_in_string(day_schedule))


print(check_schedule_day())
