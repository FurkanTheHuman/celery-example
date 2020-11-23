from tasks import easy, medium, hard
from tasks import fib_generator


task_list = [
        ("easy",easy), 
        ("medium",medium), 
        # ("hard",hard), 
        ]



for name,task in task_list:
    print("task:", name, "started")
    task.delay()

for i in range(10, 35):
    print("example task initiated, COMPLEXITY:",i)
    fib_generator.delay(i)



