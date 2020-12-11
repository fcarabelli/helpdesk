## Docker 
docker-compose down

docker rmi helpdesk_web

docker-compose up

docker-compose exec web python manage.py collectstatic

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser


