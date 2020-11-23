# Celery example for distributed task processing

This is an example project to demonstrate how does celery work on multiple worker nodes

First install celery:
`$ pip3 install celery`

## Explanation
In this project there is a worker node(acting as consumer, tasks.py) and a task producer(producer.py). 
Also this project uses redis as  a broker and a result backend
Since this project is for demonstration just use docker images:   
`$ docker run -d -p 6379:6379 redis`   



To see multiple worker nodes in action start worker nodes from terminal with:   
`$ celery -A tasks worker -l INFO -n node1@%h`  
`$ celery -A tasks worker -l INFO -n node2@%h`   
Notice that names are different. For more details on worker node creation see: https://docs.celeryproject.org/en/stable/userguide/workers.html


Now run the `producer.py` with `python3 producer.py`   
In this file we send tasks that calculates fibonacci numbers recursively, which is a very slow way to calculate it.
In the celery console, you can see that tasks distributed to different workers. This distribution happens via redis.

Even though this project works on a singular machine, once you create a redis service accesible from different machines, just update the urls for them and everything is same.

## Note 
I added yaml files for deployment to kubernetes however other way should still work. Will update after I fix some details.