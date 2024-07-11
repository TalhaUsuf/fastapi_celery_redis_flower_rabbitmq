import time
import random
import os
from celery import Celery
from celery.utils.log import get_task_logger


user = os.getenv('RMQ_USER')
pwd = os.getenv('RMQ_PWD')

celery = Celery(
    "tasks",
    # broker=f"amqp://{user}:{pwd}@rabbitmq:5672//",
    # backend="redis://redis:6379/0",
)

celery.conf.update(
    # Broker settings (assuming you're using Redis as a broker)
    broker_url=f"amqp://{user}:{pwd}@rabbitmq:5672//",

    # Using MongoDB as the result backend
    result_backend='mongodb',

    # MongoDB settings
    mongodb_backend_settings = {
    'host': os.environ['MONGO_HOST'],
    'port': int(os.environ['MONGO_PORT']),
    'user': os.environ['MONGO_USER'],
    'password': os.environ['MONGO_PASSWORD'],
    'database': os.environ['MONGO_DB'], # results (clery backend) will be stored in this DB, including all meta data
    'taskmeta_collection': 'task_results',  # collection where task specific results will be stored
    'options': {
        'ssl': False,
    },
}

)


celery_log = get_task_logger(__name__)


@celery.task
def send_email(email: str):
    time.sleep(random.randint(1, 4))
    celery_log.info("Email has been sent")
    return {
        "msg": f"Email has been sent to {email}",
        "details": {
            "destination": email,
        },
    }
