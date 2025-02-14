## cloud
- collection of data center 

## services modules
- saas:
    - software as a service 
    - like Google mails 

- paas:
    - platform as a service
    - provider: OS
    - customer: application 

- iaas:
    - intastrure as a service
    - provider: Network and storage
    - customer OS ans APP 

## cloud options 
- public:
    - azure, aws 

- private:
    - you make your own data center 

- hybrid:
    - rent from azure for some data 
    - for important data we store the data in on-premise data center 

## virtualization 
- hypervisar would seperate the server logically to make as if there is a lot of server avaliable

## load balancer
- divide the work on the servers 

## auto scaling 
- there would be other VM with the same configuration
- which can be used if the load increased 

## resouce groups 
- it is a part of the subscription
- we collect similar resoures in group 
- we can enforce same configuration on this resouces

## resource manager 
- it uses different providers to provide / create the resouces we need 

## storage 
- Blob 
    - container storage 
    - unstructured data 
    - image, videos, source code 

- file
    - more than one vm try to use this file system

- tables
    - nosql data
    - key value pairs 

- queues
    - 

## vnet 
- vnet peering:
    - we allow two vnets communicate with each other 

- vpn gate way:
    - we connect on-premise to the azure network 

## NSG
- network security group 
- it is similar to firewall 
- we define ingoing and outgoing rules 

### rules 
- source / destionation ip 
- source / destionation port
- protocol 
- rules with lower number [high priotrity] which matches would be applied  

## ip
- public:
    - it is the ip which is connected to the internet  

- private:
    - it is ip which is used inside the azure

## azure VM
- it is part of iaas
- OS disk:
    - where the OS is installed 

- Data disk:
    - logs
    - another application 

### avaliability
- zone:
    - in different building 

### connect to VM 
- RDP:
    - remote desktop protocol 

## ARM 
- azure resouce manager 

## IAM
- idenity access managment 
- AD:
    - active directory 

- authentication:
    - check if the person has a valid ID

- authorizaion:
    - check if the person is allowed to do this thing

# DevOps 
