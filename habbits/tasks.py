from datetime import datetime, timedelta

from celery import shared_task

from habbits.models import Habbit
from habbits.services import send_telegram_message


@shared_task
def task():
    """Периодическая задача отправки уведомлений в телеграмм за 5 минут до начала выполнения привычки"""
    habbits = Habbit.objects.all()
    for habbit in habbits:
        if habbit.user.chat_id and habbit.time <= datetime.now().time() - timedelta(
            minutes=5
        ):
            text = f"мне нужно {habbit.action} в {habbit.time} в {habbit.place}"
            send_telegram_message(text, habbit.user.chat_id)