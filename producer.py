from tasks import easy, medium, hard
from tasks import fib_generator


task_list = [
        easy, 
        medium,
        hard
        ]



for task in task_list:
    task.delay()

for i in range(10, 35):
    fib_generator.delay(i)



