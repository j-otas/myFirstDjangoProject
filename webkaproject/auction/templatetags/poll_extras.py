from django import template
from time import strftime
from time import gmtime
from django.utils import timezone
register = template.Library()
import datetime


@register.filter(name = "delta_time")
def deltaTime(value):
    time = value-timezone.now()
    secs = time.total_seconds()
    if secs <=0:
        return None
    timetot = ""
    days = 0
    hrs = 0
    mins = 0
    if secs > 86400:  # Сутки
        days = secs // 86400
        timetot += "{} Дней".format(int(days))
        secs = secs - days * 86400

    if secs > 3600: # Час
        hrs = secs // 3600
        timetot += " {} Часов".format(int(hrs))
        secs = secs - hrs * 3600

    if secs > 60:
        mins = secs // 60
        secs = secs - mins * 60
        if (days <= 0 or hrs<=1):
            timetot += " {} Минут".format(int(mins))

    if secs > 0:
        if days <= 0 and hrs <= 0:
            timetot += " {} seconds".format(int(secs))

    return timetot