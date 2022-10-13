# Docker

## Pré-requis du déploiement des conteneurs

- Spécifications du conteneur à déployer
    -- un logiciel d'exécution de l'application (NodeJS)
    -- Ressources nécéssaire à la l'éxécution du conteneur (CPU,Memoire,Réseaux)
- Choix de l'outil de déploiement (Docker)
- Sur quel environment on déploie (Machine Physique, Machine Virtuel)

## Les composants du logiciel Docker

- Docker Container Runtime
    Composant docker nous permettant d'éxécuter les conteneurs Docker.

Notes:
    CGroups (Control Group) - cgroups (control groups) est une fonctionnalité du noyau Linux pour limiter, compter et isoler l'utilisation des ressources (processeur, mémoire, utilisation disque, etc.).

- Docker REST API - Interface de communication de l'environment docker avec l'environment externe.

Notes:
    REST API: Une API REST (également appelée API RESTful) est une interface de programmation d'application (API ou API web) qui respecte les contraintes du style d'architecture REST et permet d'interagir avec les services web RESTful. L'architecture REST (Representational State Transfer) a été créée par l'informaticien Roy Fielding.

- Docker CLI - Utilitaire en ligne de commande permettant d'interagir avec les composant de l'environment Docker via le REST API.

- Docker Hub - Les régistres de image Docker

- Docker Swarm - Outil d'orchestration d'un groupe de comteneur

## Images/Conteneur

- Images - C'est le modèle du conteneur à déploier
- Conteneur -  Une instance d'une image s'éxécutant ou non sur moteur de gestion des conteneurs

## Configure des images docker

`Dockerfile` sont des fichiers de configuration d'une image devant être créer.

## Les command docker

> docker build -t <NOM_IMAGE> <CHEMIN_VERS_DOSSIER_CONTENANT_LE_FICHIER_DOCKERFILE> -> Nous permet de créer une image Docker

> docker image ls -> Liste les image disponible en local sur docker

> docker run -p <PORT_HOST>:<PORT_CONTENEUR> <IMAGE_NAME> -d

> docker container ls - List des conteneur disponible dans un environment donné

> docker ps -a - List les conteneur déployés sur une machine donné (En execution ou non)
