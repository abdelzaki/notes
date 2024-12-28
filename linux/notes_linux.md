### shell  1:05
- shell is interpreter which pass command to the OS
- types of shell such as bash or sh  

- lsb_release -a:
    - to get the version of the OS 

- ide to write files:
    - nano:
        - it is the easiest to create and write the files 

    - vi:
        - i -> insert mode 
        - :wq -> write and exit 
        - :q! -Y exit without saving 
    

- change users:
    - su - username 
        - change to this user 
    - su 
        - change to root 

- permissions:
    - owners of the folder/ files are user, group, others 
    - permissions are read write execute 

    - read:
        - file can be read 
        - ls command on folder 

    - execute:
        - file can be executed 
        - cd command on the folder  

    - owner is the person who created the file 

    - chown user:group folder  
        - chown ese:ese /temp/test
        - to change the owner 
        - can be done only by the root 

    - chmod ug=rwx,o+x
        - chmod ug=rwx, o=r /temp/test 
        - to change the permissions
        - owner and the root can change permissions 

- users:
    - id username 
        - would show the groups which this id belongs to 
    
    - useradd -m "username" -G sudo
        - would add the user and create home directory to it and add it to sudo group 

    - userdel -r user 
        - would delete this user 

    - usermod user
        - would change the user  

- process:
    - anything which can run 
    
    - to run process in the background & 
        - command & 
    
    - to end a process:
        - kill pid 
        - kill -9 pid -> this cannot be caught 
    
    - ps aux
        - show all the process 

    - ps -ef
        - would show the parent and children of the process  

- systemctl:
    - we use it to manage daemon in systemd 
    - systemd is the init process 

    - systemctl start/stop/enable/disable/restart daemon 


### prompt 
- username@machine_name
- # -> root 
- $ -> normal user 

### simple commands
- date
    - show the date 

- ncal
    - show the calender 

- df 
    - show the free blocks 

- exit
    - end the session 

- cd - 
    - go to the previous path 

- ls -lhA
    - h for human 
    - A for almost all 

- file "filename"
    - give information about the file 

- less "filename"
    - see the content of the file 
    - to exit write q 

- cp -i  file1 file2 
    - if file2 exists the system would ask us 

- cp -rv folder1 folder3 
    - r-> copy for folders
    - v-> verbose show what are being copied 
