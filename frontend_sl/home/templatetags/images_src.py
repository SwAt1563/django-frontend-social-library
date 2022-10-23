
from django import template

register = template.Library()

# cuz we can't see the images when the src is http://backend-sl
def localhost(src):
    HOST = 'backend-sl'
    return str(src).replace(HOST, 'localhost')

register.filter(localhost)