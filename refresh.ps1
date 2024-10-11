If (Test-Path db.sqlite3) {
    Remove-Item db.sqlite3
     Write-Host "db.sqlite3 removed"

}
If (Test-Path tutorials/quickstart/migrations) {
    Remove-Item snippets/quickstart/migrations/0*.* -Recurse -Force -Confirm:$false
    Write-Host "migrations removed"
}
python manage.py makemigrations
python manage.py migrate
$env:DJANGO_SUPERUSER_USERNAME="admin"
$env:DJANGO_SUPERUSER_PASSWORD="books@123!"
$env:DJANGO_SUPERUSER_EMAIL="test@gmail.com"
python manage.py createsuperuser --noinput
python manage.py runserver
