# atlantic-project
To use this project:
source env/bin/activate
pip install django
pip install djangorestframework
pip install drf-nested-serializer

then make migrations and migrate

python manage.py makemigrations subscriptionsproject
python manage.py migrate

and then run the server

python manage.py runserver
