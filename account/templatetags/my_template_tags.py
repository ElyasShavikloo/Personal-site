from django import template
import datetime

register = template.Library()


@register.filter(name='cutter')
def body_cutter(val, arg):
    return val[:arg]


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
