python manage.py makemigrations
python manage.py migrate
$env:DJANGO_SUPERUSER_USERNAME="admin"
$env:DJANGO_SUPERUSER_PASSWORD="books@123!"
$env:DJANGO_SUPERUSER_EMAIL="test@gmail.com"
python manage.py createsuperuser --noinput
python manage.py runserver
