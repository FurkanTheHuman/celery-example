from tasks import easy, medium
from tasks import fib_generator
from tasks import sleeper, dyn_sleeper 
from tasks import shutdown 
from time import sleep
from tasks import app 
import logging
import sys

meta = app.control.inspect()

def get_celery_worker_status():
    i = app.control.inspect()
    availability = i.ping()
    stats = i.stats()
    registered_tasks = i.registered()
    active_tasks = i.active()
    scheduled_tasks = i.scheduled()
    result = {
        'availability': availability,
        'stats': stats,
        'registered_tasks': registered_tasks,
        'active_tasks': active_tasks,
        'scheduled_tasks': scheduled_tasks
    }
    return result

def wait_for_the_workers():
    meta = app.control.inspect()
    counter = 2
    worker_num = meta.ping()
    while worker_num == None or len(worker_num) < 2:
        logging.warning(f"Workers are not up. Waiting for {counter} seconds")
        sleep(counter)
        worker_num = meta.ping()
        print(worker_num)
        counter += 2
        if counter >36:
            logging.critical(f"Workers are dead. Job failed.")
            return False
    return True


if not wait_for_the_workers():
    sys.exit(1)

task_list = [
        ("easy",easy), 
        ("medium",medium), 
        # ("hard",sleeper), 
        ]

task_state = []

for name,task in task_list:
    print("task:", name, "started")
    task_state.append(task.delay())

for i in range(10, 15):
    print("example task initiated, COMPLEXITY:",i)
    task_state.append(fib_generator.delay(i))


for i in range(1, 10, 2):
    print("example task initiated, SLEEP:",i)
    task_state.append(dyn_sleeper.apply_async(args=[i], task_id="hello_world"))



print("num of tasks:", len(task_state))

# while True:
#     completed_tasks = [task for task in task_state if task.ready() ]
#     if len(completed_tasks) ==len(task_state):
#         print("All tasks finished.")
#         for c in task_state:
#             print(">> ",c.name, c.args," :", c.result)
#         break
#     sleep(1)
active = meta.active()
#while True:
#    print(active)
#    active = meta.active()
#    tasks = list(map(lambda x: active[x], active.keys()))
#    if len([item for sublist in tasks for item in sublist]) == 0:
#        print("DONE")
#        break
#    sleep(2)

sleep(10)

print("shutting down")
x = shutdown.delay()
x.get()

print("Exiting gracefully")
print(dir(task_state))

