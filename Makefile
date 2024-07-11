.PHONY: build up down start logs_celery logs_app down_kill down uplog

build:
	@docker-compose build 

up:
	@docker-compose up -d

uplog:
	@docker-compose up 

down_kill:
	@docker-compose down --remove-orphans -v --rmi all  

down:
	@docker-compose down 


start:
	@docker-compose up --build 

logs_app:
	@docker logs celery_test_fastapi_app


scale:
	@docker-compose up --scale celery_worker=5 -d 