from celery import Celery
import os
redis_url = os.getenv("REDIS_SERVICE_URL", default="redis://localhost")

app = Celery('tasks', backend=redis_url, broker=redis_url)



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


# easy task
@app.task
def easy():
    return fib(32)

# medium task
@app.task
def medium():
    return fib(35)

# hard task
@app.task
def hard():
    return fib(40)

if __name__ == '__main__':
    app.start()
