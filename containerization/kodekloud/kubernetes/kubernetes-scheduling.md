# Kubernetes Scheduler

> kubectl get all [--selector <key>=<value>] - Returns all api resources matching a certain criteria

## Manually Scheduling a pod on a node

* How scheduling works?

All pods have a `spec.nodeName` field which is not set by default. When the pods is started, K8's assign a node name to the pod at runtime.

K8's sheduler loop though all pods to find those without `spec.nodeName` at runtime.

**Note**
Pods without `spec.nodeName` are candidate to scheduling. Using a pre-defined algorithm, the scheduler schedule the pod (Bind the pod) on a Node.

**Note**
To manually schedule a `Pod` to a given K8's `Node` , we must specify the `spec.nodeName` in the pod configuration file

or at runtime:

We create a `Pod` binding file and send a request to the REST API for the kubernetes runtime to bind a `Pod` to a `Node` .

```yml
apiVersion: v1
kind: Binding
metadata:
    name: <pod_name>
target:
    apiVersion: v1
    kind: Node
    name: <node_name>
```

The request looks like:

> curl --header "Content-Type:application/json" --request POST --data '{"apiVersion": "v1", "kind": "Binding", "metadata": {"name": "<pod_name>"}, "target": {"apiVersion": "v1", "kind": "Node", name: "<node_name>"}}' http://<SERVER_HOST>/api/v1/namespaces/default/pods/<POD_NAME>/binding/

## Labels & Selectors

Label & Selector helps in categorizing(Label) & filtering(Selectors) kubernetes object.

```yml
#...
metadata:
    # ....
    labels:
        # Configure the object labels
        app: APP_NAME
        function: Backend


# In an object that must select the previously defined object (a.k.a replicaset, deployment, services, etc...)
#...
metadata:
    #...
    labels:
        name: rs_webservice

spec:
    replicas: n
    selector:
        matchLabels:
            app: APP_NAME # Select the object labelled APP_NAME in it definition file
```

> kubectl get pods --selector <KEY>=<VALUE> - Returns the pods matching a given criteria.

**Note**
Labels are defines in k8's Object `metadata.labels` field and selectors are located at `spec.selector.matchLabels`

-- Annotations (`metadata.annotations`)

They are used to record other details or informations about the object.

```yml
#...
metadata:
    # ....
    labels:
        # Configure the object labels
        app: APP_NAME
        function: Backend
    annotations:
        buildVersion: 1.4
        # Other information parameters of the obeject
# Specs
```

## Taints & Tolerations
