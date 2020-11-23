FROM python:3.8.1-slim

RUN pip3 install celery
RUN pip3 install redis

WORKDIR /worker
COPY tasks.py /worker


CMD ["celery", "-A", "tasks", "worker", "-l", "INFO"]