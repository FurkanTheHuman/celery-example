import os
redis_url = os.getenv("REDIS_SERVICE_URL", default="redis")
redis_password = os.getenv("REDIS_PASS", default="password")
print("redis_password:",redis_password)

class Config:
    enable_utc = True
    broker_url = 'redis://:'+redis_password+'@'+redis_url+':6379/0'
    result_backend = 'redis://:'+redis_password+'@'+redis_url+':6379/0'
    result_extended=True
    task_serializer = 'json'
    result_serializer = 'json'
    event_serializer = 'json'
    accept_content = ['json']
    result_accept_content = ['json']

