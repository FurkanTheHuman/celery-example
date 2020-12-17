FROM python:3.8.1-slim

RUN pip3 install celery
RUN pip3 install redis

WORKDIR /worker
COPY tprod.py /worker
COPY test.py /worker
COPY celery_config.py /worker

CMD ["celery", "-A", "test", "worker", "-l", "INFO"]