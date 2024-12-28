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
    - it is the image when it is ran 
    
- Container would user the Kernel to run the services 

- every container has main process which would have id 1 if this process exists the container would exit 

- make sure that the user is added to Docker group so that we do not have to always write sudo when we run docker commands  

# commands
- docker image pull "image_name"
    - docker image pull python 
    - would pull python image from the web 

- docker container run -it "image_name" "command name "
    - docker container run -it python /bin/bash
    - this would run a python image 

- docker container ls 
    - would show all active docker containers 

- docker image ls 
    - would show all images