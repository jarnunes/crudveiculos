from django import template
from app.python.utils import Format
import datetime

register = template.Library()


@register.filter(name='decimalf')
def format_decimal(val, decimal_places=2):
    return Format.decimal(val, decimal_places)


@register.filter(name='currencyf')
def format_currency(val):
    return Format.price(val)


@register.filter(name='datef')
def date_format(date: datetime):
    return Format.date(date)


@register.filter(name='datetimef')
def date_time_format(date_time: datetime):
    return Format.date_time(date_time)
