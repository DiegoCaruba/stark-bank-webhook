# Run Celery

## Redis Docker Container

### Build and run local container REDIS
> docker run --name redis -d -p 6379:6379 redis

### Test connection
> docker exec -it redis redis-cli ping

- If test output contains "PONG", it was successful

## Run Celery Work
> celery -A config worker --loglevel=info 

## Run Celery Beat
> celery -A config beat --loglevel=info

