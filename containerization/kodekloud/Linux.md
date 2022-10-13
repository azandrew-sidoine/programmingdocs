# Linux/Unix OS

## Commands

> docker exec <CONTAINER_ID> <TEST_COMMAND> [<COMMAND_OPTIONS>]

> docker exec 7834689792467 ps -eaf - List all processes on the container

## Networking

> ip link - Returns the networking interfaces being used

> ip add <NET_INTERFACE> - The ip address and other informations about the network interface

-- Routing

Unix OS has an utility command for querying the kernel routing table.

> route - Display the information in the OS routing table

> ip route add 192.168.2.0/24 via 192.168.1.1 - Add - Tells the we can access 192.168.2.0 network from 192.168.1.x network

For instance to acess an internet resource:

> ip route add 95.179.195.55 192.168.1.1 - Route any request to 95.179.195.55 through 192.168.1.1

Note: Because we can not configure all website routing... We can add a catch all route to be routed through 192.168.1.1 as follow:

> ip route add default 192.168.1.1
or
> ip route add 0.0.0.0 192.168.1.1

- Setting Linux host router

Let takes this network:

(A) ----(Net 1)---- (B) --------(Net 2)------- (C)

To make it possible for (A) to send packets to (C):

-- Step 1: Add a routing to (A) and (C) to use (B) as Gateway.

-- Step 2: Make (B) to be able to forward packet from (Net 1) to (Net 2) by:
    - > `echo 1 > /proc/sys/net/ipv4/ip_forward` - This is a temporary config
    > `net.ipv4.ip_forward = 1` - Make the change persistent in /etc/sysctl.conf

- DNS (Domain Name System)

Unix system has a local file DNS server accessible at `/etc/hosts`

-- Pointing a host to a DNS Server

> vi /etc/resolv.conf
Add entry to by:

```conf
# nameserver <DNS_SERVER_IP>
nameserver 192.168.1.100

# Specify a search query to map to a doamin name
search mycompany.com # This will map to existing mycompany.com if user ping web and web is not found in /etc/hosts
```

-- Changing the DNS resolution

We all know by default that hosts look for name in /etc/hosts. By the order can be change in `/etc/nsswitch.conf` file:

```conf
# hosts     dns files - This search the DNS first
hosts:      files dns
```

-- Records Types

They are DNS entry that helps in ip resolutions:

> A - Webserver ->  IPV6 - To Server mapping
> AAAA - Web Server -> IPV6 - To Server mapping
> CNAME - Name mapping -> Mapping domain name to domain name. Ex: food.mycompany.com mycompany.com

-- NsLookup

Used to query domain name to an ip address. It bypass `/etc/hosts`. It only looks in DNS server configurations

> nslookup

-- Dig

Domain name resolution . Similar to NsLookup but withe specific implementations

> dig google.com
