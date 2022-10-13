# Docker swarm (Docker Orchestration Engine)

Docker uses `cgroups` or `Control Groups` to restrict hardware resources used by the container.

> docker service ls - List available service in the cluster
> docker service ps <SERVICE_ID> - Status of a given service

## Basics

Setting up docker swarm requires application devops to have a swarm Manager (Master node), and worker/slave nodes to sync with the master node.

To initialize swarm:

> docker swarm init [--advertise-addr <IP_ADDR>] - Initialize docker swarm cluster

- advertise-addr - Allow to specify the network interface to listen to when host has multiple interfaces

Next:

> docker swarm join --token <CLUSTER_TOKEN> - Must be run on each node to let them join the cluster

- Miscelanous

-- Cluster status

> docker node ls

-- Request token syntax to add node as worker

> docker swarm join-token worker

-- Removing a node from cluster

> docker swarm leave

-- Removing Node from master node

> docker node rm <NODE_ID>

-- Add a new master node to the cluster

> docker swarm join-token master - Return a token syntax for a node to join as manager

When that is done, copy and paste the generated syntax to the other master node and execute.

### Manager node

Docker cluster is implemented using Distributed Consensus implementation.

It's responsible for:

- managing state of container accross all workers
- Distributing workload accross all workers

Note:
For fault tolerance, we must have mutiple management nodes, by one is responsible for make management decision at time (The Leader).

The leader will continuously notify other manager node for any update in the worker node, else the cluster will fall into an inconsistent state.

Take a Look at the RAFT (Distributed Consensus) algorithm.

Decisions:

-- How many manager nodes - Odd number of manager
    Quarum of N = Ceil((N/2) + 1) -> The minimum number of member that must be in an assembly to make a vote valid in that assembly.

Note:
    Docker recommend a maximum of 7 managers per cluster. Adding more master node does not increase performance nor scalability.

> docker swarm init --force-new-cluster - Will Create a new cluster from this worker manager node if the cluster fails

> docker node promote <NODE_NAME|ID> - Promote a worker to be elligible for management

> docker node update --availability drain <NODE_NAME|ID> - Dedicate a node as only a management node

Recommendation:
    Dedicate management nodes as management only node in production environment

## Docker swarm orchestrator

Docker services are on or more instance of an application or services that runs accross a swarm cluster.

> docker service create --replicas=3 <IMAGE_NAME> - Runs a full docker image instance (container) on worker processes on the cluster

Note: `docker service create` takes same parameters as a docker run command, with added specific options.

- Tasks

When a service is started, the orchestrator decide of how many tasks to create or runs to create containers, and the scheduler schedule those tasks to be run.

Tasks are processes running on the worker node that start containers. It's a one-to-one relationship with the worker node, 1 task per node.

If the tasks container fails, the task fail as well and the master instruct creation of a new task.

- Replicas

Replicas are the number of application running.

- Replicas vs Global

`--replicas` option creates a set of predefined instance of the application

`--mode global` Create a single instance that is placed on all worker nodes.

- Updating services

> docker service update --replicas=n <IMAGE_NAME|IMAGE_ID>
