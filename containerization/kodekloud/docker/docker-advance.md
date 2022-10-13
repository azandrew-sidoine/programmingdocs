# Docker advance course

## Commands

> docker system df -v -> Show images and space consumption

## Docker on windows

- Docker Toobox (Windows (x64), Support VT)

Original docker environment for Windows. It runs docker inside a Linux virtual machine, with a set of tools for working easily with the container.

- Docker for Windows

Uses Microsoft Hyper-V as virtualization platform therefore require Windows 10 Professional Edition or Windows Server 2016 supports docker for windows by default.
By default it run Linux based containers, by can also provides using Windows based container.

-- Windows containers

Container Types:

Windows Server: Works like container running on Linux. It creates an environment where containers share OS Kernel resources.

Hyper-V Isolation: Each container runs in it completly isolated environment with it OS-Kernel.
    Hyper-V Isolation based images:
        - Window Server Core
            Windows server core OS without the UI.
        -  Nano Server
            Headless deployment OS running at the fraction at the size of the Operating System. It's like alpine verion of windows server

--- Running Windows based container

Right click the Docker icon in the right end of the taskbar, and click of the Switch to Windows Container in the pop-up menu.

## Advance Networking

- Overlay Network

With docker swarm we are able to create a VPN (Virtual Private Network) `overlay` which that passed accross containers running in the cluster.

> docker network create --driver overlay --subnet 10.0.9.0/24 <NETWORK_NAME>

To use the overlay network accross container instances:

> docker service create --replicas=n --network <NETWORK_NAME> <IMAGE_ID>

- Ingress Network (Auto with docker swarm)

It comes to rescue when more container running on the same worker uses the same port. Docker provides through ingress networking a load-balancer for redirecting external traffic to internal container instances.

The Ingress Network, Create a `routing mesh` on workers allowing `worker nodes` to redirect requests they can't handle to other `worker nodes`.

- Embedded DNS

All containers has an internal routing table that route to other container usinf their service/container names.
