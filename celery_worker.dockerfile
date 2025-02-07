FROM python:3.9
WORKDIR /app
COPY ["requirements.txt", "/app/"]
RUN pip install $(cat requirements.txt | grep -E "celery|redis|mongo")
COPY ["celery_worker.py", "/app/"]
CMD ["celery", "-A", "celery_worker.celery", "worker", "--loglevel=info"]
