from datetime import datetime

from task_2.celery import app
from celery import shared_task

from .models import Card



@shared_task
def find_expired_cards():
    """
    Функция находи просроченные карты и удаляет их
    Вызывается раз в сутки в полночь
    """
    current_date = datetime.now()
    Card.objects.filter(end_of_activity__lte=current_date).delete()