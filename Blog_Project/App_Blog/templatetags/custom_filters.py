from django import template

register = template.Library()
@register.filter
def range_filter(value):
    
    return value[0:500] + '.....'
