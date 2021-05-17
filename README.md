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

to test

    python manage.py test
    
Schema

![test](https://user-images.githubusercontent.com/21280975/118487053-546c8c80-b6e8-11eb-93f7-ef95b76166a8.png)

Things I wanted to add but didn't have enough time to 

    Testing for Gifts/Subscriptions (Duplicates/Gets)
    Adding Serializer/View for Gift and Subscriptions (To add read endpoint)
    adding git ignore/git hook/Linter for code quality
