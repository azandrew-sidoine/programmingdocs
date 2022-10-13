# Docker Stacks

Docker stacks uses a docker-compose.yml file to deploy docker cluster. Instead of using docker service command, we use `docker stack` command:

> docker stack deploy

## What is a docker stack

Resume:
    - Docker container is an instance of docker image running

    - Docker service is a collection of docker container instances running on single or multiple nodes

    - Docker stacks a group of docker services running in a given cluster
        Example: 3 instance of a node.js application, 1 instance of a Redis container and 2 instance of Database server

- Configuration file

In version 3 docker compose support a `deploy` to configure swarm deployment stack.

```yml
version: '3'
services:
    redis:
        image: redis
        deploy:
            # Number of instance of the container to be deploy
            replicas: n
            # Define the hardware resource consumption constraints
            # for the container instance
            resources:
                limits:
                    cpu: .01
                    memory: 50M
    db:
        image: mysql
        deploy:
            replicas: ...
            # Placement decides on which node the container
            # instance is places
            placement:
                # We can configure multiple constraints
                constraints:
                    - node.hostname == node1 # Place the container instance on a node with hostanme equals node1
                    - node.role == manager # Place the container on a manager node

    ...
    worker:
        image: worker
        deploy:
            replicas: 1
```
