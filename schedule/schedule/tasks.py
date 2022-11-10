from celery import shared_task
from celery.utils.log import get_task_logger

from .sms_sender import send_sms

logger = get_task_logger(__name__)


@shared_task
def send_sms_from_twilio_number_task():
    logger.info("Sent the SMS")
    return send_sms()
