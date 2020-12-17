from celery import Celery
import os
from time import sleep
from kombu.common import Broadcast

redis_url = os.getenv("REDIS_SERVICE_URL", default="redis://localhost")

app = Celery('tasks', backend=redis_url, broker=redis_url)
app.conf.update(
   result_extended=True
)
# This is not possible, class is not json serializable 
# class TestX:
#     var = 3
# 
# @app.task
# def return_obj():
#     return TestX()
#app.conf.task_queues = (Broadcast('broadcast_tasks'),)
#app.conf.task_routes = {
#    'shutdown': {
#        'queue': 'broadcast_tasks',
#        'exchange': 'broadcast_tasks'
#    }
#}
def fib(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)

# general task
@app.task
def fib_generator(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)

@app.task
def sleeper():
    print("sleep 30 task started")
    sleep(30)
    return 30

@app.task(bind=True)
def dyn_sleeper(self,s):
    print('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(
            self.request))
    print(f"dyn_sleep {s} task started")
    sleep(s)
    return s

# easy task
@app.task
def easy():
    return fib(32)

# medium task
@app.task
def medium():
    return fib(35)


@app.task(bind=True, name='shutdown')
def shutdown(self):
    # app.control.revoke(self.id)
    print(dir(self))
    app.control.shutdown()



# hard task
@app.task
def hard():
    return fib(40)

if __name__ == '__main__':
    app.start()
