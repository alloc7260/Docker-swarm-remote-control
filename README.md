# Docker-swarm-remote-control

## Controlling services on docker swarm remotely

### Prerequisites 
- Docker swarm with manager and worker nodes

### Steps to go on
1. configure `app.py` if you want any custom changes
2. build docker image and push it to docker hub in a public repository (not necessary) 
3. pull image on manager node or build it there
4. run given commands in `commands.sh` in manager node terminal to create flask and visualizer services

### Steps to use
1. You can watch the visualizer on port 8080 of manager node's localhost to gain insights about current state of swarm and running containers
2. you can use curl requests given in `curl` to create or delete sercvice or read logs of running service

### Constraints
* api key given in `commands.sh` must be send with every curl request in the json body