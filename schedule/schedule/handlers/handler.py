from datetime import datetime

schedule = {
    1: "04:00-08:00,12:00-16:00,20:00-00:00",
    2: "08:00-12:00,16:00-20:00,00:00-04:00",
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
    today = datetime.now().isoweekday()
    if today % 2 == 0:
        return display_schedule(schedule_in_string(schedule[2]))
    else:
        return display_schedule(schedule_in_string(schedule[1]))
