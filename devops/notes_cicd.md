# github actions 
- we create a yaml folder under the following path:
    - .githubs/workflows/filename.yaml 

## secrets:
    - we store the password and user name in Github itself 
    - we access them using ${{ secrets.username_docker }}

## job:
    - consist of steps which run serial 
    - jobs run parallel to another job 
    - runs where we define at which operation system it can work 
    -     

## actions
    - uses: actions/checkout@v2
        - pull the repo on the system which it can be compiled at it 
        - uses mean we are calling an action 

    - run:
        - step which would run to shell  
        - run means we execute this shell command

    - run: |
        - pip allows it to use multi lines commands 

## runners:
    - OS which would run on 
    - runs-on: ubuntu:latest 
        - the code would run on ubuntu  

## attributes:
    - name at the beginning of the file:
        - name of the workflow

    - on:
        - defines the trigger of an action 

    - push:
    - pull_request:
        -  trigger of the branches 

    - needs:
        - this make this job run after the job it needed 

    - workflow_dispatch:
        - button which can trigger the actions 

    - workflow_call:
        - this workflow is a subroutine which can be called from another routine
        - we define inputs which is needed for this workflow 
        - with keyword is used to pass values to this workflow 


## types:
    - we use it as a filter on the trigger 
    ex:
        on:
        label:
            types:
            - created

        - trigger happens on the creation of a label 

## env:
    - it is a map {key ,value}
    - the map would be avaliable to the jobs and steps 
    - ex:
        env:
            SERVER: production

## defaults:
    defaults:
        run:
            shell: bash 

    - this would be added to all the jobs 

# jenkin
    - automation tool 
    - to install jenkin in docker:
        - docker run --privileged -u 0 -p 8080:8080 -p 50000:50000 -v path_locally:/var/jenkins_home jenkins/jenkins_lts

    - SCM:
        - source control management 

## build types 
    - freestyle:
        - we create the job using GUI
        - shell that is runs 

    - piplines:
        - consist of stages which we define based on commands we write  
    - 