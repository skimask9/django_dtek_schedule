import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule.settings")
app = Celery("schedule", include=["schedule.tasks"])


app.config_from_object("django.conf:settings")


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


app.conf.beat_schedule = {
    "everyday-10:30": {
        "task": "schedule.tasks.send_sms_from_twilio_number_task",
        "schedule": crontab(minute="30", hour="10"),
    }
}
