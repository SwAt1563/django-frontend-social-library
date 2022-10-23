from django import template
from datetime import datetime
register = template.Library()


def d_m_y(date):
    print(date)
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')
    nice_format = date.strftime('%d/%m/%Y')
    return nice_format

register.filter(d_m_y)