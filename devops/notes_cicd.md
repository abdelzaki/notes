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
    - if the job exit with non zero value means the job has failed 

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

## outputs  
    - we define variable which can be used by another job 

    outputs:
        - output1: ${{ steps.step1.outputs.var1 }}
    
    steps:
        - id: step1
        - run echo "var1=value" << $GITHUB_OUTPUT


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
        - jobs:
            job1:
            job2:
                needs: job1
            job3:
                if: ${{ always() }}
                needs: [job1, job2]
        
        - always()
            - means job3 would run after job1 and job2 even if they are failed

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
    - the map would be avaliable to all jobs and steps 
    - ex:
        env:
            SERVER: production 

## matrix 
    - job would run for all the values of the matrix 
    - if we have more than one matrix the job would run for every combination
    - jobs:
        example_matrix:
            strategy:
            matrix:
                os: [ubuntu-22.04, ubuntu-20.04]
                version: [10, 12, 14]
            runs-on: ${{ matrix.os }}
            steps:
            - uses: actions/setup-node@v4
                with:
                node-version: ${{ matrix.version }}

## if
- if : always()
    - means this job would always run even if the job which is needed is skipped or failed  


## defaults:
    defaults:
        run:
            shell: bash 

    - this would be added to all the jobs 

# jenkin
## agent    
    - device which would execute the code 
    - agent none


## maven
- add maven job
- provide:
    - test report 
    - increment builds 
    - post build 

## workspace 
- for every job there is a workspace which would be created 
- we find workspace under 
    - /var/lib/jenkins/workspace 

- we should make sure that we have jave
    - to check that we have java
        - java -version 
    
    - automation tool 
    - it makes pipeline to execute different stages  

    - to install jenkin in docker:
        - docker run --privileged -u 0 -p 8080:8080 -p 50000:50000 -v path_locally:/var/jenkins_home jenkins/jenkins_lts

    - SCM:
        - source control management 

## build types 
    - freestyle:
        - we create the job using GUI
        - shell that is runs 

    - piplines:
        - it is a way to restore the step with the code in source control managment
        - consist of stages which we define based on commands we write  
        - script which tell jenkins what to do 
        - we write it in Jenkinsfile 
    - 
### docker
- we can use docker with jenkins that jenkins run inside docker 
    - ex:
        pipeline 
        {
            agent { dockerfile true }
            stages {
                stage('Test') 
                {
                    steps 
                    {
                        --
                    }
                }
            }
        }

### multibranch
- it is a way to collect more than one pipeline in the same folder

### pipeline 
- input: 
    - we write input parameter before the steps 
    - ex:
        pipeline 
        {
            agent any
            stages 
            {
                stage('Hello') 
                {
                    input 
                    {
                        message "What is your first name?"
                        ok "Submit"
                        parameters {
                        string(defaultValue: 'Dave', name: 'FIRST_NAME', trim: true) 
                    }
                    }
                    steps
                    {
                        echo 'Hello World'        
                    }
                }
            }
        }

- timeout:
    - we can put timeout around the step 
    - ex:
        options 
        {
            timeout(time: 10, unit: 'SECONDS') 
        }
        steps 
        {
            --
        }

- enviromental:
    - we can store the variable inside this scope
    - ex:
        pipeline 
        {
            agent any
            environment 
            {
                DISABLE_AUTH = "true"
                DB_ENGINE    = 'sqlite'
            }

            stages 
            {
                stage('Build') 
                {
                    steps 
                    {
                        echo "Database engine is ${DB_ENGINE}"
                        echo "DISABLE_AUTH is ${DISABLE_AUTH}"
                        sh 'printenv'
                    }
                }
            }
        }


- parameter 
    - we can add parameter to the jekins as input
    - ex:
    pipeline 
    {
        agent any
        parameters 
        {
          string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        }
        stages 
        {
            stage('Example') 
            {
                steps 
                {
                    sh "echo Hello ${params.PERSON}"
                }
            }
        }
    } 

- changeset:
    - we can run the step according to a speicifc changeset 
    - ex:
    stage("change)
    { 
        when 
        { 
            changeset " **/readme.md" 
        }         
        steps 
            { 
                echo 'rrrrr'
            }
    }
