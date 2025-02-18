## kubernets:
    - automation tool for deploying and scaling 

## features:    
    - scability 
    - self healing 
    - rollout and rollback 

## architecture 
    - pod:  
        - it is abstraction layer above the container 
        - the user doesnot need to communicate with the container but with the pod which is the abstraction layer above the container  
        - pod contains one container or more containers which share the same resources 
        - it has container Runtime 
        - pod can be stopped 
        - every pod implement a single service 

    - service 
        - it is an ip address which is connected to the pod 

    - ingress:
        - it has the domain name 
        - it it is a load balance 
    
    - configMap
        - it has configuration of your application 
        - we can connect it to the pod 

    - secret
        - it is used to store secret data 
        - we can connect it to the pod 

    - volume
        - attach visual storage to the pod 

    - deployment
        - it is a template for the pod 
        - which can replicate the application 
        - we can scale down or up the pod 

    - statefulset
        - for apps which has database
        - snchrnoise the read and write step  

    - cluster:
        - group of similar node 

    - master:
        - 

## worker node
    - provide running envirmoental for your application 
    - every node should have container runtime 

    - kubelet:
        - it has interface with container and the machine which run this container 

    - kube proxy:
        - it is the network interface 

    - worker nodes:
        - contains one or more pod 

## master node
    - it provides control plane for managing the cluster 
    - configuration data is saved in etcd 

    - api server:
        - intercepts Restful calls from user 
        - get command from the user 
        - receive the command from kubecli 

    - scheduler:
        - assigns which pods is going to perform the task 
    
    - controller manager:
        - detect status change of the pods 

    - cloud controller manager:
        - enable clouding  

    - etcd:
        - key value store of the cluser state 
    
    - kubectl
        - command line interface

## minikube 
    - it is local cluser 
    - master and worker node runs on the local host 
    - commands:
        - minikube start 
            - this would start the minikube cluster 

    - minikube dashboard
        - would show a dashboard 

## kubectl
    - command line tool which can communicate with the api server 

    - commands:
        - kubectl get replicaset
            - would show how many pods 

    - kubectl create deployment nginx-app --image=nginx
        - create an image  

    - kubectl delete deployment --all
        - delete everything 

    - kubectl get all
        - would show everything 

    - kubectl exec -it pod_name -- /bin/bash
        - run this command inside the docker  

    - kubectl logs pod_name 
        - show the logging of the pods 

    - kubectl apply -f file.yaml
        - execute what is written in this file 

    - kubectl explain resources_type
        - would show us how to write yaml


    - kubectl scale deployment image_name --replicas=7 

## namespace 
    - it is a way to group resources 

## components
    - container runtime 
        - container runtime interface 
        - docker provice containerd 
    
    - node agent(kubelet)
        - communicate with master node 

    - proxy:
        - it is network agent[TCP, UDP]

    - addons:
        - third party packages 

## labels 
    - it is key_value pair that are attached to an object 
    - key should be unique 
    - it is added to the metadata 

## selector 
    - it is a way to select a certain component
    - --selector kex=value 
    - anythig which has a label which matchs the selector would be part of the element which is defined 

## kubectl
    - kubectl create deployment nginx-app --image=nginx
        - create an image  

    - kubectl delete deployment --all
        - delete everything 

    - kubectl get all
        - would show everything 
        - resources name is not casesenstive [pods, po, pod]

    - kubectl exec -it image_name -- /bin/bash
        - run this command inside the docker 

    - kubectl create namespace name_space
        - would create namespace

    
    - kubectl scale deployment image_name --replicas=7

    - minikube dashboard
        - would show a dashboard 

## deployment 
    - can perform 
        - scaling up/down 
        - roll out / back

    - group of identical pods 
    - deployment runs multiple replices and can automatically replace any instance if one failed 
    - commands:
        - kubectl create deployment --image=nginx nginx-app
            - create an image  

        - kubectl delete deployment --all
            - delete everything 

## replicaset
    - run multiple instance of the same pod 
    - if one pod failed the another one would be created and it takes it's place 
    - commands:
        - kubectl get rs 
            - list replicaset 

        - kubectl scale rs name_replicaset --replicas=4 
            - change number of replicas to 4 

## services 
    - expose application as a network service 
    - it has a fixed ip 
    - it provide load balance
    - types of service:
        - clusterIP:
            - it is the default type 
            - access the application only inside the cluster 
            - when two deployments inside the same cluster want to communicate

## ingress 
    - 

## condig file yaml 
    - first part:
        - declare the type and version we create 
    
    - apiVersion:
        - v1:
            - Pod
            - services 
            - Namespaces 

        - apps/v1 
            - Depolyment  
            - ReplicaSet

    - metadata:
        - name 
        - labels  
        - selector  
        - namespace

    - spec:
        - it depends on the type we create 

    - deployment has the pod in template 