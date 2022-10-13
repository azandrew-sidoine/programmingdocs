# Docker Storage

Docker container write application data to a writable Layer exposed by the docker runtime, which is tighly coupled to the host machine. The provided writable layer is not persistent therefore when container process stop running data is lost.
To interact with the writable layer, container make use of pluggable volume driver that allow them to write to filesystem or in memory.

Docker has two options to writing to filesystem and an option to write to host memory depending on the machine on which container is running:

## Volumes (Named volumes) [ `Prefered Way` ]

When running docker container with named volume attached to them, data are stored into a host filesystem `created & managed by Docker` itself. Non-Docker processes must not attempt to modify such data.
Named volume data are stored in `/var/lib/docker/volumes` on unix OS.

> docker volume create [<VOLUMNE_NAME>] - create a docker storage volume. without the name parameter, a random uniquely volume name is generated within the given host.

> docker volume prune - Removes unused docker volumes.

**Note**
When you mount the volume into a container, this directory is what is mounted into the container. This is similar to the way that bind mounts work, except that volumes are managed by Docker and are isolated from the core functionality of the host machine.

**Note**
Volumes also support the use of volume drivers, which allow you to store your data on remote hosts or cloud providers, among other possibilities.

* Creating & Managing volumes

> docker volume create [<VOLUME_NAME>]

* Inspecting docker volume & Querying volumes

> docker volume inspect <volume_name>
> docker volume ls
> docker inspect <CONTAINER_NAME> - Checks if the volume is created and mounted successfully into the container. It provides more information about the running container.

* Mounting volumes to container

> docker create -d --name devtest --mount source=<VOLUME_NAME>, target=</Path> nginx:latest

> docker create -d --name devtest --volume <VOLUME_NAME>:</Path> nginx:latest

* Removing docker volumes

> docker volume rm <VOLUME_NAME>

* `mount` vs `v` flags

`-v` or `--volume` flags are legacy way to mount a volume in a container. In recent versions, docker provide a more explicit flag to mount volume in container, which is using `--mount`

syntax:

> docker create --name <CONTAINER_NAME> --volume <VOLUME_NAME>:<CONTAINER_PATH> <IMAGE_NAME>

> docker create --name --mount '[type=volume|bind|tmpfs], src=volume_name_or_bind_path, dst=container_path, [readonly], [volume-opt=type=nfs, volume-opt=device=<nfs-server>:nfs:path], [, "volume-opt=o=addr=<nfs-address>, vers=4, soft, timeo=180, bg, tcp, rw"]'

**Note**
`nfs` a.k.a `Network File System` are only required to bind with remote storage drivers.

-- `volume-opt` : Only required for volume configuration options.

**Note**
`docker service create` does not support `-v` flag. We should use the `--mount` flag to mount volumes.

### Readonly access

For some development applications, the container needs to write into the bind mount so that changes are propagated back to the Docker host. At other times, the container only needs read access to the data. Remember that multiple containers can mount the same volume, and it can be mounted read-write for some of them and read-only for others, at the same time.

### Shared file storage

This configuration allows multiple replicas to have access to same shared resource.

There are several ways to achieve this when developing your applications. One is to add logic to your application to store files on a cloud object storage system like Amazon S3. Another is to create volumes with a driver that supports writing files to an external storage system like NFS or Amazon S3.

### Use volume driver

To shared data using `nfs` storage, we must make use of docker storage plugins. `vieux/sshfs` is an SSH based implementation of volume driver.

> docker plugin install --grant-all-permissions vieux/sshfs - (Install the `vieux/sshfs` volume plugin)

* Creating a volume using a driver (Example `vieux/sshfs`)

> docker volume create --driver vieux/sshfs -o sshcmd=<USER>@<HOST>:/directory/path -o password=secret8 <VOLUME_NAME>

Same volume can be created when starting a container using the command below:

> docker run -d  --name <CONTAINER_NAME>  --volume-driver vieux/sshfs  --mount src=<VOLUME_NAME>, target=/app volume-opt=sshcmd=<USER>@<HOST>:/directory/path, volume-opt=password=secret <IMAGE_NAME>

**Note**
`-o` allow to pass data to volume drivers
`--driver` allow to specify the volume driver to use

* Using NFSV3 Volume

This example uses `REMOTE_SERVER_ADDR` as the NFS server and `/var/docker-nfs` as the exported directory on the NFS server.

```sh
docker service create -d \
  --name nfs-service \
  --mount 'type=volume,source=nfsvolume,target=/app,volume-driver=local,volume-opt=type=nfs,volume-opt=device=:/var/docker-nfs,volume-opt=o=addr=<REMOTE_SERVER_ADDR> \
  nginx:latest
```

* Using NFSV4 volume

```sh
docker service create -d \
    --name nfs-service \
    --mount 'type=volume,source=nfsvolume,target=/app,volume-driver=local,volume-opt=type=nfs,volume-opt=device=:/var/docker-nfs,"volume-opt=o=addr=<REMOTE_SERVER_ADDR>,rw,nfsvers=4,async"' \
    nginx:latest
```

* Using CIFS/Samba volumes
You can mount a `Samba` share directly in docker without configuring a mount point on your host.

```sh
docker volume create \
    --driver local \
    --opt type=cifs \
    --opt device=//<SMB_SERVER_PATH> \
    --opt o=addr=<SM_SERVER_ADDRESS>,username=uxxxxxxx,password=<PASSWORD>,file_mode=0777,dir_mode=0777 \
    --name <VOLUME_NAME>
```

### Backup and restore

Volumes are useful for backups, restores, and migrations. Use the `--volumes-from` flag to create a new container that mounts that volume.

In the example below, backup is preformed using linux tar utility from ubuntu container.

* Volume backup

> docker run -v /<VOLUME_NAME> --name <CONTAINER_NAME> ubuntu /bin/bash - Create a container named dbstore. Mount `/<VOLUME_NAME>` host directpry

> docker run --rm --volumes-from <CONTAINER_NAME> -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /<VOLUME_NAME>

* Restore volume from backup
With the backup just created, you can restore it to the same container, or another that you made elsewhere.

> docker run -v /<VOLUME_NAME> --name <CONTAINER2_NAME> ubuntu /bin/bash

> docker run --rm --volumes-from <CONTAINER2_NAME> -v $(pwd):/backup ubuntu bash -c "cd /<VOLUME_NAME> && tar xvf /backup/backup.tar --strip 1"

* Pros:

-- Provide ways to shared data amoung container. When volume are created and attached to a container, when that container is destroyed, the volume still exist in docker fs.

-- Decoupled from host fs layer & managed by docker itself

-- Provides a way store data remotely (Cloud providers driver)

-- When you need to back up, restore, or migrate data from one Docker host to another, volumes are a better choice. You can stop containers using the volume, then back up the volume’s directory (such as /var/lib/docker/volumes/<volume_name>)

-- When your application requires high-performance I/O on Docker Desktop. Volumes are stored in the Linux VM rather than the host, which means that the reads and writes have much lower latency and higher throughput.

-- When your application requires fully native file system behavior on Docker Desktop. For example, a database engine requires precise control over disk flushing to guarantee transaction durability.

## Bind Mount (fs mapping)

Container running in a bind mount configuration, stores their data anywhere on the Host Operating system, manageable by other os processes.

Available since the early days of Docker. Bind mounts have limited functionality compared to volumes. When you use a bind mount, a file or directory on the host machine is mounted into a container.

Bind mount volumes are kind of tighly coupled to Host filesystem layer.

### Mounting container

With bind-mount, `bind-propagation` key of the `--mount` flag allow to change the bind propagation. Possible values are `rprivate|private|rshared|shared|rslave|slave`.

* Mount Empty directory
If you bind-mount into a non-empty directory on the container, the directory’s existing contents are obscured by the bind mount. This can be beneficial, such as when you want to test a new version of your application without building a new image.

* Use a read-only bind mount
For some development applications, the container needs to write into the bind mount, so changes are propagated back to the Docker host. At other times, the container only needs read access.

```sh
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app,readonly \
  nginx:latest
```

### Configure the selinux label

If you use selinux you can add the z or Z options to modify the selinux label of the host file or directory being mounted into the container. This affects the file or directory on the host machine itself and can have consequences outside of the scope of Docker.

* The `z` option indicates that the bind mount content is shared among multiple containers.
* The `Z` option indicates that the bind mount content is private and unshared.

### Bind mount with docker compose

```yml
version: "3.9"
services:
  frontend:
    image: node:lts
    volumes:
      - type: bind
        source: ./static
        target: /opt/app/staticvolumes:
  myapp:
```

### Pros

-- Sharing configuration files from the host machine to containers. This is how Docker provides DNS resolution to containers by default, by mounting /etc/resolv.conf from the host machine into each container.

-- Sharing source code or build artifacts between a development environment on the Docker host and a container. For instance, you may mount a Maven target/ directory into a container, and each time you build the Maven project on the Docker host, the container gets access to the rebuilt artifacts.

-- When the file or directory structure of the Docker host is guaranteed to be consistent with the bind mounts the containers require.

**Note**
It is created on demand if it does not yet exist. Bind mounts are very performant, but they rely on the host machine’s filesystem having a specific directory structure available.

> docker create --volume <bind_mount|named_volume>:<container/path> <IMAGE_NAME>

## In-Memory (tmpfs/npipe)

Docker on Linux, `tmpfs` mount is used to store files in the host’s system memory. If you’re running Docker on Windows, `named pipe` is used to store files in the host’s system memory.

**Note**
Data saved to `tmpfs` is not written to host filesystem.

* named pipes

An `npipe` mount can be used for communication between the Docker host and a container. Common use case is to run a third-party tool inside of a container and connect to the Docker Engine API using a named pipe.

> docker create --tmpfs <IMAGE_NAME>

## Configure bind propagation

Bind propagation defaults to rprivate for both bind mounts and volumes. It is only configurable for bind mounts, and only on Linux host machines. Bind propagation is an advanced topic and many users never need to configure it.

Documentation is provided at [https://docs.docker.com/storage/bind-mounts/#configure-bind-propagation]
