from django import template
from time import strftime
from time import gmtime
from django.utils import timezone
register = template.Library()
import datetime


@register.filter(name = "delta_time")
def deltaTime(value):
    time = value-timezone.now()
    return strftime("%H:%M:%S", gmtime(time.seconds) )
