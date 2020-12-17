from test import dyn_sleeper 
from time import sleep
import codecs
import pickle
import base64
from test import Num
from test import var


task_list = []
def serialize_input(inp):
    return base64.b64encode(pickle.dumps(inp)).decode('utf-8')
for i in range(5, 15, 2):
    print("example task initiated, SLEEP:",i)
    task_list.append(dyn_sleeper.delay(serialize_input(Num(i))))

# codecs.encode(pickle.dumps(model), "base64")
# deserialize -- > pickle.loads(codecs.decode(pickled_model, "base64"))

print("num of tasks:", len(task_list))

while True:
    completed_tasks = [task for task in task_list if task.ready() ]
    if len(completed_tasks) ==len(task_list):
        print("All tasks finished.")
        for c in task_list:
            print(">> ",c.name, c.args," :", c.result)
        break
    print("There is", len(completed_tasks), "completed tasks out of", len(task_list), "tasks")
    print(">> ", len(completed_tasks)/len(task_list)*100)
    sleep(1)
    
sleep(10)
