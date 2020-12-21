# Helpdesk


Application developed in django to record and answer user queries

##Prerequisites and Dependencies

* Python3 https://docs.python.org/3/
* Django https://www.djangoproject.com/
* Django Simple Captcha https://django-simple-captcha.readthedocs.io/
* Django Bootstrap 4 https://django-bootstrap4.readthedocs.io/en/latest/
##

## Installation Steps

### Clone the repo
```bash
git clone https://github.com/fcarabelli/helpdesk
```
###

### Upgrade pip and create virtual enviroment
```bash
pip3 install -U pip

pip3 install virtualenv

virtualenv --help

virtualenv venv . 

venv\Scripts\activate

pip3 install -U pip

```

###


### Install dependencies

```bash
pip3 install -r requirements.txt
```
###

### Make migrations
```bash
manage.py makemigrations
```

### Migrate
```bash
manage.py migrate
```

### Run the server
```bash
manage.py runserver
```

##Prerequisites and Dependencies


### Django Q
```bash
python manage.py clusterq

python manage.py migrate

python manage.py runserver
```



## Application Components

There are 2 apps actually:

* helpdeskapp

* session


##

###Helpdeskapp

This application registers the questions of the users.
Questions are made through the AddQuestion form.



###Session

It is responsible for recording the activity of authenticated users

###



## Usage


##

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
