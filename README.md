# Running Linux commands in Django

To run this demo

```shell
cd /to/here
docker-compose up

# terminal inside the Docker web_* container
python manage.py migrate django_celery_results
python manage.py runserver

# another terminal inside the Docker web_* container
celery -A app worker -l INFO
```

Some gotcha
- Rerun celery worker after updating celery tasks. Rerunning Django app does not work.
- Don't use RabbitMQ RPC as celery result backend if we want to share celery task result between views
