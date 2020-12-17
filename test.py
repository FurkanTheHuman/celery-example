from celery import Celery
import os
from time import sleep
import codecs
import pickle
import base64

from celery_config import Config
app = Celery('algorithms')

redis_url = os.getenv("REDIS_SERVICE_URL", default="redis://localhost")
redis_password = os.getenv("REDIS_PASS", default="password")
if True:
    app.config_from_object(Config)
else:
    app = Celery('tasks', backend=redis_url, broker=redis_url)




app.conf.update(
    result_extended=True,
    task_serializer = 'json',
    result_serializer = 'json',
    event_serializer = 'json',
    accept_content = ['json'],
    result_accept_content = ['json']
)

class Num:
    def __init__(self, no):
        self.no = no 
    def comp(self,x):
        self.no = x**2
        return self.no

var = {
    "hello": "world",
    "sayi":3
}


# def deserialize_input(func):
#     def task(df):
#         df = base64.b64decode(df)
#         df = pickle.loads(df)
#         df = pickle.dumps(func(df))
#         df = base64.b64encode(df)
#         
#        return df
#    return task

def deserialize_input(func):
    def dec(x):
        return func(pickle.loads(base64.b64decode(x.encode("utf-8"))))
    return dec


@app.task()
@deserialize_input
def dyn_sleeper(s):
    print("!!!!!!!!!!!!!!!!!!!!")
    print(s.no)

    sleep(5)
    
    return s.no
