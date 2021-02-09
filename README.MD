# Helpdesk #


Application developed in django to record and answer user queries

## Prerequisites and Dependencies ##

* Python3 https://docs.python.org/3/
* Django https://www.djangoproject.com/
* Django Simple Captcha https://django-simple-captcha.readthedocs.io/
* Django Bootstrap 4 https://django-bootstrap4.readthedocs.io/en/latest/
* Celery https://docs.celeryproject.org/en/stable/
* Redis https://pypi.org/project/redis/


## Installation Steps ##

1.  Create redis container
```bash
sudo docker run --name redis -p 6379:6379 redis:latest
``` 

2.  Install celery and redis dependencies
```bash
sudo venv/bin/activate
pip install celery[redis]
```

3. Run django
```bash
python manage.py migrate
python manage.py runserver
```


4. Run worker at terminal
```bash
celery -A helpdesk worker -l INFO
```


