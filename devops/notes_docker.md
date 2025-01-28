- docker is a software which implement container technology 

- Devops:
    - build the VM 
    - operate the VM 

- hypervisor:
    - it is responsible for versitualize the HW 

- docker files:
    - files which are used to build docker image 

- Image:
    - it is a build docker files which can be ran 

- container:
    - it is the image when it is ran, run time instance of the image 
    
- Container would user the Kernel to run the services 

- every container has main process which would have id 1 if this process exists the container would exit 

- make sure that the user is added to Docker group so that we do not have to always write sudo when we run docker commands  

- every docker has an IP address which can be used so the containers can communicate with each other on the host system 

- registry:
    - it is the place where the images are stored 

- image name:
    - it is repo:tag

# network 
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
    - docker run --network bridge 
    - here the docker is connected to network type bridge 

# docker file
- it is the file which is used to write command of which can be used to build docker image 
- it starts always from from ubuntu:22.04 as base image 
- the command starts with RUN 
- to build:
    - docker build -t tag:name path 

# docker compose
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

# commands
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
    -it             -> interactive terminal  
    --net           -> to connect docker to a specific network 
    --ip            -> to assign container to a specific ip

- docker network create --subnet=172.18.0.0/16 my_net
    - to create network with a specific subnet 


- docker container ls 
    - would show all active docker containers 

- docker image ls 
    - would show all images

- docker image/container inspect "image name" 
    - would show us the data of the docker files 

- docker tag source_image target:tag  
    - this would create a tag from this image 

- docker build -t name_of_image path_of_docker_file
    - this is used to build an image from a docker file 

- docker run
    - this would run this command inside the image while building

- CMD 
    - this command would run whien the image is built and can be overrwritten by the docker run command

- ENTRYPOINT
    - this would run when the image is built and it cannot be overwritten but command can be appended to it 

- docker container exec -it container_name bash 
    - this would open terminal on the container 