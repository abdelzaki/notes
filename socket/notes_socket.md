## general 
- Sockets represent endpoints in a line of communication.
- when we create a socket we get a file descriptor which we can use to send and receive 
- a file descriptor is used to refer  both to a file open or to a socket 
- function read and write can operator on both file or socket 

## socketpair 
- fd = socket(domain, type, protocol);

- domain:
    - here we use AF_ -> address family 
    - AF_UNIX:
        - means the address will be formed according to linux rules
        - communication between application on the system host  

    - AF_INET:
        - the address will be formed according to the IP rules 
        - applications run on a different hosts 


- protocol:
    - this should be zero to allow the OS to choice the right protocol 

- type:
    - SOCK_DGRAM
        - when we want to use UDP 
    
    - SOCK_STREAM
        - TCP



struct sockaddr {
    sa_family_t sa_family; /* Address family (AF_* constant) */
    char sa_data[14]; /* Socket address (size varies according to socket domain) */
};

## unix domain socket 
- struct sockaddr_un {
    sa_family_t sun_family; /* Always AF_UNIX */
    char sun_path[108]; /* Null-terminated socket pathname */};

- we cannot bind to an existing pathname 
- we should use unlink after the path is not needed
- we bind UNIX domain sockets to path_names in the /tmp