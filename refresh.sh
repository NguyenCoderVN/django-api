python manage.py makemigrations
python manage.py migrate
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=books@123!
export DJANGO_SUPERUSER_EMAIL=admin@littlelemon.com
python manage.py createsuperuser --noinput
python manage.py runserver
