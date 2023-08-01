web: gunicorn sms_backend.wsgi:application --log-file - --log-level debug
python manage.py collectstatic
manage.py migrate