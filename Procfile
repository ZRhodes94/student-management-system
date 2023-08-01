web: gunicorn sms_backend.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
C:\Users\ZRhod\OneDrive\Desktop\student-management-system\student_management_system\static