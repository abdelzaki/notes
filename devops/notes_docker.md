- docker is a software which implement container technology 

- Devops:
    - build the VM 
    - operate the VM 

- hypervisor:
    - it is responsible for versitualize the HW 

- docker files:
    - files which are used to build docker image 

- Image:
    - it is compiled docker files 

- container:
    - run time instance of the image 
    
- Container would user the Kernel to run the services.

- docker desktop:
    - software in Windows 
    - allow us to create linux container or windows container  

- every container has main process which would have id 1 if this process exists the container would exit 

- make sure that the user is added to Docker group so that we do not have to always write sudo when we run docker commands  

- every docker has an IP address which can be used so the containers can communicate with each other on the host system 


- image name:
    - it is repo:tags

- bash -c "echo hi; bash ":
    - means run this command in bash and return bash 

## registry
- registry:
    - it is the place where the images are stored 

- docker login 
    - to login with user name and pass 

- docker tag image_old abdel/image_name:v1 
    - create tag for this iage 

- docker image push abdel/image_name:v1 
    - would push this image to the registry

## network 
- for every docker container we create a virtual adapter would be created on the host machine 
- Network types:
    - Bridge:
        - container has his own ip and ports which are not mapped to the external world 
        - we have to map the ports to the external world if we want to communicate with them 

    - host:
        - the container would mapped automatically to the host device 
        - all ports are mapped automatically to the host ports 

    - none: 
        - the container is isolated we cannot communicate with the container from the outside world 

- we can create a connection [virtual connection] 
    - docker network create --subnet 10.0.0.0/16 name_of_network 

- containers which are connected to the same network can communicate with each other 

- we can connect the connection to the container 
    - docker network connect connection container 
    - as if the container has another network device another ethernet device 

- docker container would by default connect to bridge connection

- we can connect to a specific network
    - docker run --network network_name 
    - here the docker is connected to this network 

- docker network connect / disconnect "network_name" docker_name
    - we connect this docker to this network 
    - we can connect more than one network to the same container 

## volumes 
- to mount the folder
    - doker container run -v path_host:path_docker "image_name"

- docker volume create "volume_name"
    - this would create volume

## docker file
- it is the file which is used to write command of which can be used to build docker image 
- it starts always from from ubuntu:22.04 as base image 
- the command starts with RUN 
- to build:
    - docker build -t tag:name path 

- RUN
    - this would run this command inside the image while building
    - -y:
        - this would say yes to the input of this command 
    - bash file.sh

- CMD 
    - this command would run when the image runs and can be overrwritten by the docker run command
    - CMD ["./src/file.sh"]


- ENTRYPOINT
    - this would run when the image is built and it cannot be overwritten but command can be appended to it 
    - ENTRYPOINT ["/bin/bash", "-c"]

- WORKDIR /app 
    - create app directory and move to it 

- ENV key=value
    - this would create enviromental variable 
    - would be used inside the docker container after the iamge is built 

- ARG VAR=VALUE
    - this would create variable which we can use this inside the docker file 

## docker compose
- it is a way to combine image + voume + network 
- we can create network and volumes using docker-compose
- service can communicate with each other using the name of the service if they are hosted on the same Network 

- docker compose --version
    - would check if is installed 

- docker-compose.yml
    - the file in which we write the compose  

- port is mapped -> HOST_PORT:CONTAINER_PORT

### keys
- image: app:latest

    - docker image which we would run

- build: ./folder   
    - if the image is not built, build the service from this folder

- depends_on: another_service 
    - this service wont start untill the other service starts

- command: sh -c "./app && cd /foler"

- consist of:
    - version 
    - services
    - networks
    - volumes 

- it enable us to run more than one service 
- profile:
    - services which has profile wont run automatically when we call docker-compose up 
    - docker compose --profile name_of_profile up
- to overwrite the command of the docker compose
    - docker-compose run "name_of_profile" bash 

## logs
    - we can see the logs of the container 
    - docker container logs name_of_container 
        - would show us the logs of the container 

## commands
- docker image pull "image_name"
    - docker image pull python 
    - would pull python image from the web 

- docker container run -it "image_name" "command name "
    - docker container run -it python /bin/bash
    - this would run a python image 

- docker container run:
    -p              -> map host port to port inside the docker container 
    -d              -> detach so the docker would run in the background 
    --name          -> would give a name to the container 
    --add-host      -> name:ip to give hostname and ip address to the docker 
                    -> we can ping this name or the ip address 
    -it             -> interactive terminal  
    --net           -> to connect docker to a specific network 
    --ip            -> to assign container to a specific ip
    -e              -> enviromental variable 

- docker container cp source_file dockername:path_inside_docker:
    - this would copy file from host machine to a docker container 

- docker network create --subnet=172.18.0.0/16 my_net
    - to create network with a specific subnet 

- docker container ls 
    - would show all active docker containers 
    -a  -> would show all containers

- docker image ls 
    - would show all images

- docker image/container inspect "image name" 
    - would show us the data of the docker files 

- docker tag source_image target:tag  
    - this would create a tag from this image 

- docker build -t name_of_image path_of_docker_file
    - this is used to build an image from a docker file 

- docker container exec -it container_name bash 
    - this would open terminal on the container 

- docker container / iamge rm "name_of_container"
