from django import template
import datetime

register = template.Library()

@register.filter
def stringformat(value, args):
    return datetime.strptime(value, args)