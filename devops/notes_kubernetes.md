## kubernets:
    - automation tool for deploying and scaling 

## features:    
    - scability 
    - self healing 
    - rollout and rollback 

## architecture 
    - cluster:
        - group of similar node 

    - master:
        - 
## worker node
    - provide running envirmoental for your application 

    - worker nodes:
        - contains one or more pod 

    - pod:
        - contains one container or more containers which share the same resources 
        
        - it has container Runtime 

### components
    - container runtime 
        - container runtime interface 
        - docker provice containerd 
    
    - node agent(kubelet)
        - communicate with master node 

    - proxy:
        - it is network agent[TCP, UDP]

    - addons:
        - third party packages 

## master node
    - it provides control plane for managing the cluster 
    - configuration data is saved in etcd 

    - api server:
        - intercepts Restful calls from user 

    - scheduler:
        - assigns which pods is going to perform the task 

    - cloud controller manager:
        - enable clouding  

    - etcd:
        - 
    
    - kubectl
        - command line interface

## kubectl
    - kubectl create deployment --image=nginx nginx-app
        - create an image  

    - kubectl get all
        - would show everything 

    - minikube dashboard
        - would show a dashboard 

    - kubectl delete deployment --all
        - delete everything 

## pode 

