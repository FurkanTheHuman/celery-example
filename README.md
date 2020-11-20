# Celery example for distributed task processing

This is an example project to demonstrate how does celery work on multiple worker nodes

First install celery:
`$ pip3 install celery`

## Explanation
In this project there is a worker node(acting as consumer, tasks.py) and a task producer(producer.py). 
Also this project uses rabbitmq as broker and redis as result backend
Since this project is for demonstration just use docker images:   
`$ docker run -d -p 6379:6379 redis`   
`$ docker run -d -p 5672:5672 rabbitmq`   



To see multiple worker nodes in action start worker nodes from terminal with:   
`$ celery -A tasks worker -l INFO -n node1@%h`  
`$ celery -A tasks worker -l INFO -n node2@%h`   
Notice that names are different. For more details on worker node creation see: https://docs.celeryproject.org/en/stable/userguide/workers.html


Now run the `producer.py` with `python3 producer.py`   
In this file we send tasks that calculate fibonacci numbers recursively, which is a very slow way to calculate it.
In the celery console you can see that tasks distributed to different workers. This distribution happens via rabbitmq.

Even though this project works on a singular machine, once you create a rabbitmq and a redis service accesible from different machines, just update the urls for them and everything is same.

