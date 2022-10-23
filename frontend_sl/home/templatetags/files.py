
from django import template

register = template.Library()

def file_name(file):
    return str(file).split('/')[-1]

register.filter(file_name)