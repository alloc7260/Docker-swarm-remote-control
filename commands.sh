docker service create \
  --name=viz \
  --publish=8080:8080/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  dockersamples/visualizer

docker service create \
  -e API_KEY="bxwe723bt72yxn1zy2exznq3qnxxtb6tbt3r7623xn36n" \
  --name=flask \
  --publish=5000:5000/tcp \
  --constraint=node.role==manager \
  --mount=type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
  alloc7260/swarm_remote_control:v2