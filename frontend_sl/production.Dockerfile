# syntax = edrevo/dockerfile-plus
INCLUDE+ base.Dockerfile

CMD ['gunicorn', 'frontend_sl.wsgi:application', '--bind', '0.0.0.0:8000']