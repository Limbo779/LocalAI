**Docker Installation Commands (Ubuntu):**
- `sudo apt-get update` - Updates the package repository lists.
- `sudo apt-get install` - Installs prerequisite packages for Docker.
- `curl -fsSL https://get.docker.com -o get-docker.sh` - Downloads Docker installation script.
- `sh get-docker.sh` - Executes the script to install Docker automatically.
- `sudo docker version` - Checks the installed Docker version.

**Basic Docker Commands:**
- `docker run <image>` - Runs a container from an image; pulls if not present locally.
- `docker run -d <image>` - Runs container in detached (background) mode.
- `docker run -it <image>` - Runs container in interactive mode with a terminal.
- `docker run -p <host_port>:<container_port> <image>` - Maps a host port to a container port.
- `docker run -v <host_path>:<container_path> <image>` - Binds a host directory to the container (bind mount).
- `docker run --mount type=bind,source=<host_path>,target=<container_path> <image>` - Newer, verbose way to bind mount.
- `docker run -e <ENV_VAR>=<value> <image>` - Sets an environment variable inside the container.
- `docker run --cpus=<value> <image>` - Limits container CPU usage (e.g., 0.5 for 50%).
- `docker run --memory=<value> <image>` - Limits container memory (e.g., 100m for 100MB).
- `docker ps` - Lists running containers.
- `docker ps -a` - Lists all containers (including stopped ones).
- `docker stop <container>` - Stops a running container.
- `docker rm <container>` - Removes a stopped container.
- `docker images` - Lists images on the host.
- `docker rmi <image>` - Removes an image.
- `docker pull <image>` - Pulls an image without running it.
- `docker exec <container> <command>` - Executes a command inside a running container.
- `docker attach <container>` - Attaches terminal to a running container.
- `docker logs <container>` - Shows logs from a container.
- `docker inspect <container>` - Returns detailed container info in JSON format.
- `docker network ls` - Lists Docker networks.
- `docker network create --driver bridge <network_name>` - Creates a new bridge network.
- `docker volume create <volume_name>` - Creates a Docker volume for persistent storage.

**Dockerfile Instructions:**
- `FROM <base_image>` - Specifies the base image (must be first instruction).
- `RUN <command>` - Executes a command during image build (e.g., `apt-get update`).
- `COPY <src> <dest>` - Copies files from host to image.
- `ENTRYPOINT ["executable"]` - Sets the primary command run when container starts; command-line args are appended.
- `CMD ["executable","arg"]` - Provides default arguments for `ENTRYPOINT`; can be overridden at runtime.
- `EXPOSE <port>` - Documents which port the container listens on (informational).

**Docker Build & Registry Commands:**
- `docker build -t <tag> .` - Builds an image from a Dockerfile in current directory and tags it.
- `docker history <image>` - Shows the layered history of an image.
- `docker tag <image> <registry>/<image_name>` - Tags an image for a registry (e.g., `localhost:5000/myapp`).
- `docker push <image>` - Pushes an image to a registry.
- `docker login` - Logs into a Docker registry.

**Docker Compose:**
- `docker-compose up` - Starts services defined in `docker-compose.yml`.
- `docker-compose.yml` - YAML file defining multi-container applications (services, networks, volumes).
- `version: '3'` - Specifies Docker Compose file format version.
- `services:` - Root key for defining each container/service.
- `build: <path>` - Specifies directory containing Dockerfile to build image instead of pulling.
- `networks:` - Defines custom networks for services to join.
- `depends_on:` - Defines service startup order dependencies.

**Networking & Storage:**
- Bridge Network - Default private network for containers (172.17.x.x range).
- Host Network - `--network host` removes network isolation; container uses host's network.
- None Network - `--network none` gives container no network access.
- Storage Drivers - Docker uses drivers like `aufs`, `overlay2`, `devicemapper` for layered filesystems.
- Copy-on-Write - Mechanism where container writes are made to a new writable layer, preserving base image layers.
- `/var/lib/docker` - Default directory where Docker stores images, containers, volumes.

**Docker Engine & Architecture:**
- Docker Daemon (`dockerd`) - Background process managing Docker objects.
- Docker REST API - Interface for tools to communicate with the daemon.
- Docker CLI (`docker`) - Command-line tool using the REST API.
- Namespaces - Isolate processes, network, mounts, etc., per container (e.g., PID namespaces).
- Control Groups (cgroups) - Limit hardware resources (CPU, memory) per container.

**Docker Swarm (Orchestration):**
- `docker swarm init` - Initializes a node as a Swarm manager.
- `docker swarm join` - Joins a node to the Swarm as a worker.
- `docker service create --replicas <num> <image>` - Creates a service with multiple replicas across the Swarm.

**Kubernetes Basics:**
- `kubectl run` - Deploys an application on a Kubernetes cluster.
- `kubectl cluster-info` - Views cluster information.
- `kubectl get nodes` - Lists all nodes in the cluster.
- Node - Worker machine where containers run.
- Master - Node hosting control plane (API server, scheduler, controllers, etcd).
- Pod - Smallest deployable unit (one or more containers).
- `kubelet` - Agent running on each node to manage containers.

**Example Application Stack (Voting App):**
- Images: `redis`, `postgres`, `voting-app`, `result-app`, `worker`.
- Docker Run with Links (legacy): `docker run --link <container>:<alias> ...` enables communication by hostname.

**Platform-Specific:**
- Docker Toolbox - Uses VirtualBox VM (legacy for older Windows/Mac).
- Docker Desktop for Windows/Mac - Uses native hypervisor (Hyper-V/hyperkit).
- Windows Containers - Use `Windows Server Core` or `Nano Server` as base images.
- Hyper-V Isolation - Runs each Windows container in a lightweight VM for kernel isolation.