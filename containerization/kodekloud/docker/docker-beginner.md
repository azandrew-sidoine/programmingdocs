# Containerization

Docker makes creating container/container application easily for end users by abstracting away low level implementation of `Aleskey based containers`.

## Container & Virtual Machines

Container based solutions like docker:

* uses the underlying OS on which they runs, while isolating running environment of instances.
* They share OS resource and does not provide full isolation.
* Becauses they uses the underlying OS Kernel to power up running instances of the containers
* rely on OS kernel to run container instance.

Note:

    There for to run linux container on Windows or Mac, Docker destop provides a virtualized Linux kernel image that will power running container.

Virtulizers or Hypervisor:

* have complete isolated environment for running different OS on the same hardware
* Their boot type is lower higher than those of container as they have ot boot the entire OS
* They consume more space than Container, for the fact that they must have complete running isolated operating system

**Note**
From the above comparison the objectif must never been to compare or run a given technology instead of the other, but rather utilize both technologies in the same environment to scale horizontally and efficiently.

## Container vs images

* Image are template for running container, like for hypervisor we have virual machines templates

* And container are running instances of a given image.

## Getting started

* Installation of Docker

[https://docs.docker.com]

-- Docker convinience scripts

> [curl|wget] -fsSL https://get.docker.com -o get-docker.sh \

   sudo ./get-docker.sh

* Running a testing container

> docker run hello-world

## Basic commands

> docker ps [-a| `Show all running and not running containers` ] - Show the docker processses
> docker ls - List available container
> docker stop <container_id|container_name> - Stop a running container
> docker rm <container_name>
> docker images - List available images on the host system
> docker rmi <image_name|image_id> - Remove the specified image from the docker host. Note that no running container must be using images.
> docker pull <image_name> -  To download image locally

**Note**
Some images like ubuntu OS, or various OS must not have processes. In order to start a process for those images, we must issue:

> docker run <image_name> sleep <IDDLE_TIME| `in seconds` > - Docker runs image as process for a set of time and then it stop.

When we run the docker container using docker run command, the process runs in attach mode a.k.a in the current terminal which when closed will end the container process.

To run in daemon or dettach mode:

> docker run -d <image_name> -  Runs the docker container in background

To attach a daemon process:

> docker attach <container_id> - container_id is provided to user when runs with -d

## Advance container command line commands and flags

-- Docker run

--- Iterative mode

> -i  - Accepts input from terminal
> -t - Tells docker to attach a pseudo terminal

To run a container in interactive mode:

```sh
docker run -it scope/image
```

--- Port Mapping

> docker run -p <HOST_PORT>|<CONTAINER_PORT> [scope]/image

```bash
docker run -p 80:3000 drewlabs/devserver
```

--- Volumes mapping

It allows operation manager to persist container data after the container stops, exit...

> docker run -v <HOST_DIRECTORY_PATH>:<CONTAINER_DIRECTORY_PATH>

For instance, to persists mysql data directory

```bash
docker run -v /container/var/lib/mysql:/var/lib/mysql mysql
```

--- Passing environment variables

> docker run -e <ENV_VAR_NAME>=<ENV_VAR_VALUE>

-- Inspection of a container

> docker inspect <container_name>|<container_id> - Returns json formatted string of the container informations.

> docker logs <container_name>|<container_id> - Returns all logs from a container

## Docker images

Creating a docker images of application or resources helps devops teams to easily package and deploy applications easily.

Step 1:

Creating a docker image requires creating a `Dockerfile` at the root of the project.

```Dockerfile
# From which source to create the image
FROM Ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

# Copy everthing from the source directory to the container
COPY . /opt/nginx/html

# Set an environment variable during build
ENV HOME /home/sys

# Adding files to the image
ADD .bashrc /home/sys/.bashrc

# Set the container entry point
ENTRYPOINT FLASK_APP=/opt/nginx/html/app.py flask run
```

Step 2:

Run the command to build the docker image

> docker build path/to/Dockerfile -t [scope]/image-name

Step 3: [Optional] Pushing to remote docker respository

> docker push [scope]/image-name

**Note**
Docker build command is a layered architecture implementation. Each command in the dockerfile is a layer of execution that stores the changes from the previous layer before running the actual command.

To see the list of layer used to build the image:

> docker history scope/image-name

Docker will cache previous build so that it can resume from successfull layers.

## Docker ENTRYPOINT vs CMD

> CMD ["commnd", ["parm1", "param2", .... "paramn"]] - Executes a Binary when the container is run

The command of the Dockerfile can be overriden using entrypoint instructions:

Entrypoint instruction is like command instruction where we can specify the command or shell script to be run when the container starts that allow container to receive arguments and/or options.

> ENTRYPOINT ["sleep"]

TO use default argument to commands, combine ENTRYPOINT and CMD commands.

## Networking in Docker

Docker comes by default with 3 networks drivers:

* Bridge [default]

It's a private internal network created by docker that containers are attached to. Each container create within the bridge network will have an IP Address usually in the range of 172 or 17 series.

Containers must access each other using those internal IPS. Port mapping allows containers to communicate on the host.

--- Attaching network type when running the containers:

> docker run --network=<host|none|bridge>

* None

Dos not attach the container to any networks, as it runs in it owns isolation network and does not talk to any external world.

* Host

Removes the network isolation boundary between the host network and the containers network. It works like NAT (Network Address Translation).
But this brings the limit of having 2 containers running on the same port on the same docker host.

-- Creating user defined network

> docker network create --driver <host|none|bridge> --subnet <SUBNET_ADDRESS>/range <network_name>

```sh
docker network create --driver bridge --subnet 182.1.18.0.0/16 private-network
```

> docker network ls - List all available network drivers along with user defined ones

--- Embedded DNS

All containers in the docker environment can resolve each other using their names as docker has it own built-in dns server that resolver container names to their ip addresses.

## Docker storage

By default docker installation will create `/var/lib/docker` . Docker will store:

-- Containers files in `${DOCKER_ROOT}/containers`

-- Volumes in `${DOCKER_ROOT}/volumes`

For handling file access and mounting point, etc.. docker uses storage drivers:

--- AUFS - Default on Ubuntu
--- ZFS
--- Device Mapper - Better for CentOS, Fedora ...
--- Overlay
--- Overlay2

Docker chooses the default optimized storage driver for a given operating system.

    When we instruct docker to create a volume using:

> docker create volumne <volume_name>

    Docker will create a folder at this path : `${DOCKER_ROOT}/volumes/volume_name`

> docker run -v volume_name:/var/lib/mysql mysql - Volume mounting Mount and persist everything in container /var/lib/mysql folder in `${DOCKER_ROOT}/volumes/volume_name`

> docker run -v /path/to/folder:/var/lib/mysql mysql - Bind mounting allows in mounting to any location on the os.

New way of mounting volumes:

> docker run --mount type=<MOUNTING_TYPE>, source=<SOURCE_PATH>, target=<TARGET_PATH>

> docker run --mount type=bind,source=/data/mysql,target=/var/lib/mysql mysql

Example:

```bash
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=db_pass123 --mount type=bind,source=/opt/data,target=/var/lib/mysql -d mysql
```

Note: The source and target path must exists

-- Images at `${DOCKER_ROOT}/images`

**Note**
Hash is computed from command in the Dockerfile when building layers of images.

**Note**
Containers can be linked to one another using the `link` command line flags.

> --link <service_name>:<dns_name>

> docker run - d --name=<container_name> -p 3000:80 --link redis:redis webapp - Adds an entry in the /etc/hosts of the `webapp` container like:

```conf
172.17.0.2  redis <container_id>
```

## Docker Registry

Learn about how to configure and deploy docker registries

## Docker engine

Docker stack comes with a CLI, a REST API interface and Daemon. This stack is the docker engine.

* The CLI can use used on another machine to access the daemon process remotely. To do so operation user must specify the `-H` or `--host` flag:

> docker run -H 192.168.1.1 ...

* The REST API interface is for developpers to build tools for interacting, creating, etc... with docker engine.

* The daemon process is instance that manage network, volumes, containers, images, etc...

**Note**
Docker containerization is handle using namespacing.

Restricting resources used by the container can be done using:

> docker run --cpus=.5 - Tells the container to use only up  to 50% of the available processor memory. Range(.1 - 1)
> docker run --memory - Tells the container to use only 100M of the available memory
