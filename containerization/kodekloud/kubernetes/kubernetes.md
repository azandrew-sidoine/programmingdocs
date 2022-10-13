# Kubernetes

## Commands

> kubectl delete <OBJECT_KING> <OBJECT_NAME> - Delete or Remove a kubernetes cluster object.
> kubectl get all - Returns all server resources

-- `Kubectl run`

> kubectl run <CONTAINER_NAME> --image=<IMAGE_NAME> [--dry-run=client -o yaml] - Create a K8 Pod with the specified image name

When `dry-run` is specified, no container is created and the definition file is written to to a file on the OS disk

-- `kubectl create`
The `create` command is used to create K8's server objects like `ReplicaSet`, `Service`, `Deployment`, etc...

> kubectl create <OBJECT_KIND> --image=<IMAGE_NAME> <POD_IMAGE_LABEL> [--replicas=<RS_NUMN>] [--dry-run=client] -o yaml > `path/to/file`

- Editing a live deployed Pod can be done using:

1) kubectl get pod <POD_NAME> -o yaml > path/to/.yml file
2) Edit the yaml file
3) Delete previous pod
4) Recreate Pod using the modified pod definition file

## Basics

In Kubernetes cluster, we must have at least 1 master Node and 1/xple Worker Node (a.k.a Minions).

Unlike docker swarm, kubernetes runs container inside a virtual blocks called `Pods`, not directly on the worker node.

- Pods

It's a single unit of container deployment one can create. Layer of abstraction provided by kubernetes to run containers in a virtual environment.

Note: A single Pod can contains multiple container instance as long as they serve different application service but depends on each other. Example:

> Pod {Web server + Redis + Database }

Services/Conatiners inside the same pod, share same `IP Addr`, `Storage`...

Note: We do not add containers to a Pod to scale. We will always add a new `pod` with a `container` instance.

- Deployment

A deployment is like services in docker swarm. Deployment creates replicat sets that ensure that set of pods are deployed and running in the cluster.

- Services

Services enables communication between pods (Ingress Network) & with external resources.
    -- Internal - ClusterIP for communication between pods (components)
    -- External - Loadbalancer -> To expose port to external users so our services are accessible

- kubectl

Client application for interacting with and managing pods.

> kubectl run <POD_NAME> --image=<IMAGE_NAME> - Here <IMAGE_NAME> is a valid docker image
> kubectl create -f <PATH_TO_POD_DEFINITION_FILE>
> kubectl get nodes [-o WIDE] -> Get List of pods
**Note**
    READY section of the output shows the `total number of containers running in Pod / Total number of container in Pod`
> kubectl describe pods <POD_ID|POD_NAME> - Provides a more details information about the pod object
> kubectl cluster-info - Get information about kubernetes cluster

Note: Steps for creating kubernetes clusters

1) Deploy PODs
2) Create Services (ClusterIP)
3) Create Services (LoadBalancer)

## Container orchestration

Kubernetes is a tools or software for deploying and managing thousand of container to provide services High Availability and performance.
It's use to orchestrate container infrastructures.

### Architectures

- Nodes (Minions)
    They are virtual machines spin up for for running containerized application.
- Master
    It's a kubernetes node that manage worker nodes.
- Component
    K8s software is made of:
    -- API Server (Master Node) -  Acts like the front-end API interface to the K8s environment. CLI, User Developped App talks to the API Server.

    -- etcd (Master Node) - Distributed fast, flexible and secure Key-Value store, where kubernetes stores data to manage the cluster. It's responsible.

    -- Kubelet (Worker Node) -  Agent making sure containers are running on the specified node as expected. Listen for request from API Server, to perform operation on Worker Node.

    -- Kube-proxy (Worker Node) - Makes sure the necessary rules are define on worker nodes to allow communication between containers nodes. It's a Pod Network solution deployed in the cluster.

    -- Container Runtime (Worker & Master Node) - Underlying software running containers. Docker, etc...

    -- Controllers (Master Node) - Responsible of the state of container nodes. Manages availability and inavailability of container nodes. They manage bringind down or up containers.
    Monitor state of kubernetes object and, takes action based on the object state.

**Note**
    Master node(s): Manage,Plan,Schedule,Monitor Nodes.

    `Controller-Manager` : Package containing all kubernetes controller components.

    -- Sheduler - Responsible for distributing workload to the container nodes (Master Node). They identify the right node to deploy container on based specification of pods object kind definitions.

    They use the container label constraints, physical resource requirements to identify nodes.

## K8s Setup

For development and Test purpose Minikube and MicroK8s can be use to setup kubernetes.

For production grade applications, `kubeadm` must be used.

- Minikube

Minikube bundle all k8s component into a single `.iso` file that can be deploy in a local environment.

- Kubectl

The cli utility can be used to manage local/remote(production) cluster easily.

## Pods, Replicat Sets & Deployments

### Pods configuration using YAML

Kubernetes defines in yml files 4 top required configurations:

```yml
apiVersion: v1 # Defines Kubernetes api-version
        # Possible values: POD -> v1, Services: v1, ReplicatSet: apps/v1 Deployment: apps/v1
kind: Pod # Possible values: Pod,Services,ReplicatSet,Deployment

metadata: # Data about the object being created
    name: <POD_NAME> # String value representing the Pod
    labels: # Can have any key as wished by the devops
        app: <APPLICATION_NAME>
        env: production # Passing environment to the pod configuration
        type: web-service # The type of the pod which can serve to the user later

spec: # Sepecifications of the object. It properties may vary depending on the object being created
    containers:
        -
            name: nginx-container # Container name
            image: nginx
```

To create the pod:
> kubectl create -f path/to/pod/definition.yml

## Replication Controllers and Replica Sets

Controllers in the Kubernet Software are the brain of the cluster. They manage state of pod in the kubernetes cluster.

Replica Set is a set of multiple instance of kubernetes Pods.

**Note**
    `ReplicationController` is the old technology used to deploy or perform replication in kubernetes cluster.
    With recent versions of kubernetes, `ReplicaSet` is the technology recommended to use.

For replication controller definition file looks like:

```yml
apiVersion: V1
kind: ReplicationController # Possible values: Pod,Services,ReplicatSet,Deployment

metadata:
    name: "Repl Controller"
    labels:
        # Keys

spec:
    replicas: 3 # Number of replicas to deploy
    template: # Template of the pod to replicate
        # Pod definition except [apiVersion] and [kind] fields
```

> kubectl get replicationController - Returns the list of replication controllers

**Note**
    Each pod of a replication controller has it name prefix with replication controller name

Replica Set definition:

```yml
apiVersion: apps/v1 # For replica set
kind: ReplicaSet # Possible values: Pod,Services,ReplicatSet,Deployment

metadata:
    name: "Repl Controller"
    labels:
        # Keys

spec:
    # Big difference between ReplicationController and ReplicaSets
    selector: # Defines pods that fall under the replica set.
        matchLabels: # Match pods labelled with a given key:value
            type: web-service # Match Pods with labels === web-service

    replicas: 3 # Number of replicas to deploy

    template: # Template of the pod to replicate
        # Pod definition except [apiVersion] and [kind] fields
```

> kubectl get rs|replicaSet > Returns the list of replica sets in the cluster.
**Note**
    The `DESIRED` column is the number of desired Pods, while `CURRENT` is the number of currrently deployed Pods.

**Note**
    Replica set can be used to manage pods that has not been created by it, that's why we must provide a `selector` key under `spec`.

`selectors` are used by the replica set to know which pod must be monitored.

**Note**
    The template part is always required, as it's used by the replica set to know how to create new pods when failure occurs.

- Saclability

Method 1:

Here we manually update object definition file definition:

1) Change `spec.replicas` key to `n`
2) Run : kubectl replace -f <PATH_TO_DEFINITION.yml>

Method 2:

This method does not update the object definition file:

> kubectl scale --replicas=6 -f <PATH_TO_DEFINITION.yml>
or
> kubectl scale --replicas=6 replicaset <RECLICA_SET_NAME>

> kubectl scale --replicas=2 rs/<REPLICA_SET_NAME>

Method 3:

> kubectl edit <OBJECT_KIND> <OBJECT_NAME> - Kubernetes load the object configuration in memory and allow user to edit the object configuration.

**Note**
    When getting object kind definition , we can redirect it to an output file:

> kubectl get <OBJECT_KIND> <OBJECT_NAME> -o yaml > </path/to/name.yml>

### Deployments

Kubernetes deployments are used to deploy container in production environment. It provides with capabilities for performing rolling updates, perform pause changes, pause resumes etc...

> kubectl create -f <DEPLOYMENT_FILE.yml> [--record] - The `record` flag is used to log changes in deployment history

- Rolling upgrade:
    It's the king of web services/container instances upgrade done one after the order in order to not break application users flow.

Provide devops an abstraction around cluster deployment using Rolling update, Pausing for changes and Resuming as required.

Configuration file:

It's same as replicatSet with `kind` key set to `Deployment`.
There is no much difference with replicaset except it create an object of type `Deployment`.

> kubectl get deployments - Returns the deployed Deployments

### Deployments - Rollback and Versionning

**Note**
Creating a deployment always require the deployment name and the image to use for the deployment `--image`.

> kubectl rollout status deployment <DEPLOYMENT_NAME> - Returns the rollout status of the deployment
> kubectl rollout history deployment <DEPLOYMENT_NAME> -  `History and revisions of deployment`

- Deployment strategy

-- Recreate strategy: This strategy destroy and recreate all pods deployed using the deployment.
    Cons: The application may become unavailable while the strategy is processed.
-- Rolling Update (default) : Older versions are taken down one by one making the web service available during upgrade.

> kubectl apply -f <UPDATED_DEPLOYMENT_FILE_.yml>
> kubectl describe deployment <DEPLOYMENT_NAME> - For more information about the deployment

- Upgrades

> kubectl rollout undo <DEPLOYMENT_NAME> - Brings the deployment back to it previous state

**Note**
    Refers to upgrades related image in the directory.

```yml
apiVersion: apps/v1 # For replica set
kind: Deployment # Possible values: Pod,Services,ReplicatSet,Deployment

metadata:
    name: "My Deployment"
    labels:
        # Keys

spec:
    # Big difference between ReplicationController and ReplicaSets
    selector: # Defines pods that fall under the replica set.
        matchLabels: # Match pods labelled with a given key:value
            type: web-service # Match Pods with labels === web-service

    replicas: 3 # Number of replicas to deploy

    strategy:
        # Only required if type is RollingUpdate
        # rollingUpdate:
        #     maxSurge: 25%
        #     maxUnavailable: 25%
        type: RollingUpdate # Possible values are RollingUpdate,Recreated

    template: # Template of the pod to replicate
        # Pod definition except [apiVersion] and [kind] fields
```

### Networking

Unlike in docker, in kubernetes IP address is assign by the host to a POD instead of directly to containers.
Kubernetes creates an internal Private Network when install and configured that allows pods to communicate between themselves.

- Clustering Networking

The default networking configuration in a single node environment does not work well in kubernetes cluster, as having an internel networking for the cluster can cause IP conflicts.
To handle such case, kubernetes forces devops, to define the network type for the cluster:

-- All container/PODs must communicate to one another without NAT
-- All nodes must communicate wil all container and vice-versa without NAT

Fortunately, we has vmware, flannel, NSX, Cisco, etc... that provides solutions that comes to our rescue.

### Services

They are K8's objects that offer ability to decouple comunication between pods and with the outside world.
Services:

- enable communition between components within and outside kubernates.
- enable loose coupling in kubernetes infrastructures.

Kubernetes services help us perform:

-- Port forwarding to cluster Pods

#### Services commands

> kubectl create -f <SERVICE_FILE.yml>
> kubectl get services|svc - Returns the list of available services
> kubectl describe service kubernetes - To describe kubernetes service
> kubectl expose pod <pod_name> --port=<service_port> --name <service_name> --dry-run=client -o yaml - Create a Service named <service_name> of type `ClusterIP` to expose pod <pod_name> on port <service_port>

#### Services Types

**Note**
    If a pod must not be accessible by the outside world, use the clusterIP service type.
    Else if the pod must be accessible externally, use NodePort service type

- NodePort (Bridge networking)

Internal pods are accessible within the node the are running on. Accesibility is done using port mapping as in Docker.

**Note**
    NodePort port number must be in a valid range (30000 - 32767)
    Kubernetes takes in charge to load balance request to pods in the kubernetes environment.

Service object configuration:

```yml
apiVersion: apps/v1 # For replica set
kind: Service # Possible values: Pod,Service,ReplicatSet,Deployment

metadata:
    name: "My Service"
    labels:
        # Keys

spec:
    type: NodePort # Possible values: NodePort,ClusterIp,LoadBalancer
    ports:
        -
            targetPort: 80 # Pod's Port, which will take port value if missing
            # Service Port
            port: 80 # Port on the service object
            # External Port
            NodePort: 30008 # Port exposed to the outside world, If missing, an available port number will be allocated
    selector:
        # These selector must match label defines in a pod definition file
        app: PodLabelName
        type: PodLabelType
```

- ClusterIp

Kubernetes creates a virtual IP to enable communication between pods, or cluster objects.
It helps group pods and serve them from a single interface.

Pods of a group share a single communication interfaces that makes use of service's configuration. Each configured service get a `name` assigned to it that must be used by any pod or service willing to connect to it, and it `ip` address.

```yml
apiVersion: apps/v1
kind: Service # Possible values: Pod,Service,ReplicatSet,Deployment

metadata:
    name: "My Service"
    labels:
        # Keys

spec:
    type: ClusterIP # Possible values: NodePort,ClusterIP,LoadBalancer
    ports:
        -
            targetPort: 80 # Grouped Pod's port number
            port: 80 # Port on the service object
    selector:
        # These selector must match label defines in a pod definition file
        app: PodLabelName
        type: PodLabelType
```

- Load Balancer

Provision a load balancer for web services. It provides an alternative using nginx or httpProxy loadbalancers, but require to be deploy on a cloud provider infrastructure.

#### K8's Namespaces

Namespaces are isolation objects that helps manage k8's resources.

What does namespace helps in:

- Defining access policy to objects
- Constraint resource usage to a certains limit (CPU, Memory, etc... resources)

-- DNS

- To resolve object in the same namespace use `<service_name>`
- To resolve object in other namespaces use `<service_name>.<namespace>.svc.cluster.local` because when a service is created it's register with this format.
    -- `svc` - subdomain
    -- `cluster.local` - default k8's domain name

> <service_name>.<namespace>.<subdomain>.<domain>
> kubectl get <OBJECT_KIND> --namespace=<NAMESPACE_NAME> - List objects in a given namespace
> kubectl create -f <OBJECT_DEFINITION_FILE> --namespace=<NAMESPACE_NAME> - Create a k8's object in a given namespace

Note:
    K8's object can be added to a namespace by adding value to `<definition_file>.metadata.namespace`

```yml
apiVersion: v1 #
kind: Namespace # Possible values: Pod,Service,ReplicatSet,Deployment

metadata:
    name: <NAMESPACE_NAME>
```

> kubectl create -f <definition_file>
or
> kubectl create namespace <namepace_name>

> kubectl config set-context $(kubectl config current-context) --namespace=<namespace_name> - Set the current execution context to equal the <namespace_name>.
**Note**
Executing the command above permanently set the default namespace for the current terminal session

By default K8's creates a default namespace to which all objects are attached when no namespace is not defined for the object.

To prevent user from delete or altering default k8's object that kubernetes uses internally, k8 creates a `kube-system` namespace to wich system related object are attached.

`kube-plublic` is where public resource or object are attached.

-- Resources quota

To create a resources quota that will be apply to a given namespace:

```yml
apiVersion: v1
kind: ResourceQuota

metadata:
    name: <resource_quota_name>
    namespace: <namespace_name>

specs:
    pods: "n" # Total number of pods in the namespace
    requests.cpu: "n" # Requested CPU quotas
    requests.memory: 1Gi # Requested memory quota
    limit.cpu: "n" # CPU resource limit definition
    limits.memory: "2Gi" # Memory limit definition
```

> kubectl create -f <definition_file>

#### Kubernetes Admin (kubeadm)

Used to bootstrap kubernetes cluster. It's helps create and configure kubernetes cluster for production environment.

- Step to setting up a cluster using kubeadm

1) Physical/Virtual Machines that can communicate with each other (Master and Worker Nodes)
2) Install a container runtime on the node (Follow instruction on kubernetes website)
3) Install kubeadm tool on the nodes (Follow installation, requirements and configuration on kubernetes website)
4) Initialize master server
5) Configure Pod NetWork
6) Join Worker Node to cluster
7) Hooray!

- Installing kubernetes components

-- kubeadm : Bootstrap the cluster
-- kubelet : Runs on all of the machin in the cluster and does things like starting pods and containers
-- kubectl : CMD util to talk to the cluster

> sudo apt-get update && sudo apt-get install -y apt-transport-https curl
> curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
> sudo apt-get install -y kubelet kubeadm kubectl

- Kluster creation process

For the purpose follow instructions on the kubernetes website.

### Kubernetes declerative vs imperative

Running commands like `kubectl create`, `kubectl delete` or `kubectl edit` etc... ends to be an imperative approach to managing k8's objects.

K8's comes with a `kubectl apply` command which takes a declarative approach which is it reads a configuration files and apply the required changes to the k8's environment objects.

> kubectl apply -f <path/to/file_or_directory> - apply command try to find an existing object and update it if it exists, else it update it.

#### Kubectl apply

Before managing object, apply command read the local configuration file passed as parameter, the live k8's objects and the last applied configurations, before applying changes to k8's environment.
