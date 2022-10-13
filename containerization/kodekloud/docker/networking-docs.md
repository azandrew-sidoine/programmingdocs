# Docker networking

One of the powerful feature of docker Container & Services is their ability to talk to each other or to other peers (docker workload or not) in a platform agnostic way.

**Note**
To handle networking, docker manipulate `Iptables` on Linux or `Routing Table Rules` on Linux.

## Network drivers

Docker networking subsystem is pluggable (Adaptable) using drivers.

### Bridge Networking (Default)

Documentation [https://docs.docker.com/network/bridge/]

Apps runs in standalone container that need to communicate (An isolated virtual network is created by docker to allow container to communicate with each other isolated from the host network).

**Note** (Networking)
In terms of networking, a bridge network is a Link Layer device which forwards traffic between network segments. Bridge can be a hardware device or software running on host machine kernel.

Docker bridge automatically install Networking rules on Host machine to prevent container or services running on different network to communicate.

* Differences between user-defined bridges and the default bridge

-- Automatic dns resolution among containers

On user defin bridge, container access each other by using service name or alias. While on default bridge they can only access each other by ip address unless a `--link` (legacy) option has been specify when running the container.

-- User-defined bridges provide better isolation.
All containers without a `--network` specified, are attached to the default bridge network. This can be a risk, as unrelated stacks/services/containers are then able to communicate.

User defined bridge networks create an isoclation scope which only allow container in the same network to communicate.

-- Containers can be attached and detached from user-defined networks on the fly
During a container’s lifetime, you can connect or disconnect it from user-defined networks on the fly. To remove a container from the default bridge network, you need to stop the container and recreate it with different network options.

> docker network connect <carte_reseau> <nom_conteneur> - Connect un conteneur a un réseau prédéfini

-- Each user-defined network creates a configurable bridge.

User define networks are created using `docker network create` , therefore configuring it is isolated from other network configurations.

-- Linked containers on the default bridge network share environment variables.
Originally, the only way to share environment variables between two containers was to link them using the --link flag. This type of variable sharing is not possible with user-defined networks. However, there are superior ways to share environment variables. A few ideas:

> docker run --name <nom_conteneur> --link <nom_conteneur_a_connecter> - crée un lien entre un conteneur (source) et un autre conteneur

Multiple containers can mount a file or directory containing the shared information, using a Docker volume.

Multiple containers can be started together using docker-compose and the compose file can define the shared variables.

* Managing networks

> docker network create <NETWORK_NAME> [--ipv6] [--help] -> Creates a user defined bridge network. use the help option to see more options. `--ipv6` enables ipv6 addressing for docker containers (Require enbaling ipv6 networking in docker daemon).

> docker network rm <NETWORK_NAME> -> Removes network drivers from docker runtime

> docker network prune -> Removes all unused network drivers from docker runtime

> docker create --name <CONTAINER_NAME> --network <NEWORK_NAME> --publish <HOST_PORT>:<CONTAINER_PORT> <IMAGE_NAME> -> Create a container and attach it to a user defined bridge network.

> docker network connect <NET_NAME> <CONTAINER_NAME> -> Connect a running container to <NET_NAME>
> docker network disconnect <NET_NAME> <CONTAINER_NAME> -> Disconnect a running container to <NET_NAME>

* Use Ipv6

If you need IPv6 support for Docker containers, you need to enable the option on the Docker daemon and reload its configuration, before creating any IPv6 networks or assigning containers IPv6 addresses.

* Enable forwarding from Docker containers to the outside world

By default, traffic from containers connected to the default bridge network is not forwarded to the outside world. To enable forwarding, you need to change two settings. These are not Docker commands and they affect the Docker host’s kernel.

> sysctl net.ipv4.conf.all.forwarding=1 -> Configure Linux kernel to allow ip forwarding
> sudo iptables -P FORWARD ACCEPT -> Forward traffic from docker containers to outside world

* Default Bridge network (Not recommended for production)

> docker create --link redis --publish 8888:80 <IMAGE_NAME> - connect the container to default bridge and create a link to the redis service

-- Default bridge configuration (daemon.json)

```json
{
    // ...
  "bip": "192.168.1.1/24",
  "fixed-cidr": "192.168.1.0/25",
  "fixed-cidr-v6": "2001:db8::/64",
  "mtu": 1500,
  "default-gateway": "192.168.1.254",
  "default-gateway-v6": "2001:db8:abcd::89",
  "dns": ["10.20.1.2","10.20.1.3"]
  // ...
}
```

### Host network driver

For Standalone container like bridge networking, but removes the isolation introduced by the bridge driver and run the container directly on the host network.

Container run in the Host network namespace, share ip range and port.

**Note**
`-p`, `--publish`, `-P`, and `--publish-all` are ignored in host networking.
Host mode networking can be useful to optimize performance, and in situations where a container needs to handle a large range of ports, as it does not require network address translation (NAT), and no “userland-proxy” is created for each port.

The host networking driver only works on Linux hosts, and is not supported on Docker Desktop for Mac, Docker Desktop for Windows, or Docker EE for Windows Server.

> docker create --name <nom_conteneur> --network host --publish 8888:80 <nom_image>

### Overlay

Documentation [https://docs.docker.com/network/overlay/]

More dedicated to docker clusters, by communicating multiple docker daemon together and enable swarm services to communicate with each other. It allows containers running on two different docker daemon to communicate with each other.

### IPvlan

IPvlan networks give users total control over both IPv4 and IPv6 addressing. The VLAN driver builds on top of that in giving operators complete control of layer 2 VLAN tagging and even IPvlan L3 routing for users interested in underlay network integration

### MacLan (uses mac addresses to route traffic in docker environment)

Macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network. The Docker daemon routes traffic to containers by their MAC addresses. Using the macvlan driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host’s network stack.

### None

For containers that does not require communication with other services.

## Summary

* `User-defined bridge` networks are best when you need multiple containers to communicate on the same Docker host.
* `Host networks` are best when the network stack should not be isolated from the Docker host, but you want other aspects of the container to be isolated.
* `Overlay networks` are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using swarm services.
* `Macvlan` networks are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.

## Miscelanous

### Docker & Iptables

Linux Iptable is used by docker to manipulate network isolation.

How to inter-operate with docker policies in production environment:

* Add iptables policies before Docker’s rules

**Note**
Docker installs two custom iptables chains named `DOCKER-USER` and `DOCKER` , and it ensures that incoming packets are always checked by these two chains first.

Most of docker ip rules are added to the `DOCKER` chain and that chain should not be manipulate manually. Rules that must be apply before docker rules must be added to `DOCKER-USER` chain.

Rules added to the `FORWARD` chain -- either manually, or by another iptables-based firewall -- are evaluated after these chains.

**Warning**
Port that are exposed by docker container get exposed to the outside world no matter what rules are defined in the `FORWARD` chain.

* Restrict connections to Docker host

By default, all external source IPs are allowed to connect to the Docker host.

> iptables -I DOCKER-USER -i <EXTERNAL_INTERFACE> ! -s 192.168.1.1 -j DROP -> Restrict external access from all ip except from 192.168.1.1

Allowing access from subnetting:

> iptables -I DOCKER-USER -i <EXTERNAL_INTERFACE> ! -s 192.168.1.0/24 -j DROP

Finally, you can specify a range of IP addresses to accept using `--src-range` (Remember to also add `-m` iprange when using `--src-range` or `--dst-range` ):

> iptables -I DOCKER-USER -m iprange -i <EXTERNAL_INTERFACE> ! --src-range 192.168.1.1-192.168.1.3 -j DROP

You can combine -s or --src-range with -d or --dst-range to control both the source and destination. For instance, if the Docker daemon listens on both 192.168.1.99 and 10.1.2.3, you can make rules specific to 10.1.2.3 and leave 192.168.1.99 open.

iptables is complicated and more complicated rules are out of scope for this topic. See the [https://netfilter.org] HOWTO for a lot more information.

* Docker on a Router

Docker also sets the policy for the FORWARD chain to DROP. If your Docker host also acts as a router, this will result in that router not forwarding any traffic anymore. If you want your system to continue functioning as a router, you can add explicit ACCEPT rules to the DOCKER-USER chain to allow it:

> iptables -I DOCKER-USER -i <SRC_INTERFACE> -o <DEST_INTERFACE> -j ACCEPT

* Docker Integration with `Firewalld`

If you are running Docker version 20.10.0 or higher with firewalld on your system with --iptables enabled, Docker automatically creates a firewalld zone called docker and inserts all the network interfaces it creates (for example, docker0) into the docker zone to allow seamless networking.

Consider running the following firewalld command to remove the docker interface from the zone.

```sh
# Please substitute the appropriate zone and docker interface
firewall-cmd --zone=trusted --remove-interface=docker0 --permanent
firewall-cmd --reload
```
