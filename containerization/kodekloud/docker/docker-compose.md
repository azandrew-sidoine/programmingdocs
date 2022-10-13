# Docker compose


## Basics

Docker compose uses a `.yml` configuration file to build and run images and containers.

```yml
main_container:
    build: ./path/to/directory/where/Dockerfile/is/located
    port:
        8888:80
    links:
        - container_name
        - container_name2
container_name:
    image: image_name
    ports:
        # Port mapping
        - 3000:80
    links:
        # Tells to <container_name> that it's linked to <container_name2>
        - container_name2

container_name2:
    image: image_name_container_2
    ports:
        - 5001:80
```

> docker compose up -d - Docker compose will build application stack for the developper.

Docker compose starting from version 2 required specify compose version and services:

```yml
version: <VERSION_VALUE>
services:
    main:
        build: ./path/to/directory/where/Dockerfile/is/located
        port:
            8888:80
        depends_on:
            # Wait until other builds finishes before building main_container service 
            - service1
            - service2
        networks:
            - backend
            - frontend
    service1:
        image: image_name
        ports:
            # Port mapping
            - 3000:80
        networks:
            - backend

    service2:
        image: image_name_container_2
        ports:
            - 5001:80
        networks:
            - backend

networks:
    backend:
    frontend:
```

**Note**
From docker compose v2, an isolated network environment is created for application stack, there for there is no need to tell what are services linked in the stack, as compose will automatically generate it.

Version 3 add support for swarn configurations.
