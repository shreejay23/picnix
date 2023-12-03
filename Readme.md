### How it was created?

1. python3 manage.py startproject picnix
2. python3 manage.py startapp picnix_backbone

### How to setup?

1. python3 manage.py createsuperuser
2. python3 manage.py makemigrations
3. python3 manage.py migrate
4. install redis

### How to run?

1. start redis server
2. celery -A picnix worker -l info
3. python3 manage.py runserver
