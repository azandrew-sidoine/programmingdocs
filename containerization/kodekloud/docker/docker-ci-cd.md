# Docker with CI/CD

## CI/CD Pipeline

- CI - Countinuous Integration is the flow of developpers deploying a source code to a version Control system, the flow of building the application & Testing the application for errors.

- CD - Countinuous delivery/Deployment is a flow of downloading and deploying the application to production.

## Docker Registry

> docker run -d -p 5000:5000 --restart always --name registry registry:2

- Preparing to deploy docker image on a custom registry

> docker tag <LOCAL_IMAGE> <REGISTRY_URL>/<IMAGE_NAME>

- Pushing to the custom registry server

> docker push <REGISTRY_URL>/<IMAGE_NAME>

- Pulling from custom registry server

> docker pull <REGISTRY_URL>/<IMAGE_NAME>

Note:
To access the registry using web interface, we must deploy a front-end container from the docker hub.

## Docker cloud

- Docker cloud

It's docker owns cloud based container hosted applications. Docker takes in docker-compose stack file, and deploy the stack in it infrastructure, handling failover for you.
Docker uses internally cloud prodviders like AWS/Azure/Google Cloud based on developper choice.
