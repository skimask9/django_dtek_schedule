from datetime import datetime

DAYS = {"Friday","Sunday","Saturday","Monday"}



schedule = {
    1: "06:00-08:00,14:00-16:00,22:00-00:00",
    2: "04:00-06:00,12:00-14:00,20:00-22:00",
    3: "02:00-04:00,10:00-12:00,18:00-20:00",
    4: "00:00-02:00,08:00-10:00,16:00-18:00",
}


def schedule_in_string(day: str) -> str:
    normalize_day = day.split(",")
    new_day = "\n".join(normalize_day)
    return new_day


def display_schedule(d: str):
    today = datetime.now().strftime("%d.%m")
    exactly_day = datetime.now().strftime("%A")
    return f"Schedule for {today} - {exactly_day}: \n{d}"


def check_schedule_day():
    exactly_day = datetime.now().strftime("%A")
    if exactly_day in DAYS:
       return display_schedule(schedule_in_string(schedule[1]))
    elif exactly_day == "Tuesday":
        return display_schedule(schedule_in_string(schedule[2]))
    elif exactly_day == "Wednesday":
        return display_schedule(schedule_in_string(schedule[3]))
    elif exactly_day == "Thursday":
        return display_schedule(schedule_in_string(schedule[4]))

