## shell
- shell is interpreter which pass command to the OS
- types of shell such as bash or sh  

## copy and create
    - to copy a file or folder  
        - cp -r source destination     
        - cp -r folder1 ../folder2 
            - this would move the folder to the parent folder
                - if folder2 does not exist it would copy folder1 and rename it to folder2
                - if folder2 exists  it would copy folder1 inside it and the folder would still have the same name 

        - cp -r folder1 ../folder2 
            - if folder2 does not exist it would move the folder 

## change the password 
    - passwd 
        - this would change my own password 

    - sudo passwd user_name
        - this would change the password of this user 

    - sudo passwd 
        - this would change the password of the sudo user   

## change user 
    - change users:
        - su - username 
            - change to this user 
        - su - 
            - change to root 

## find 
    - find path -name "name"
        - sudo find / -name "sps" 
            - this would search the file sps in the whole system 

## link 
    - soft_link means if the original file deleted the link points to nothing and we cannot read the data anymore 
        - link -s "source" destination 
            - this would create soft link, if the source deleted the link is not valid 

    - hard_link if the source is deleted the hard_link still has the data 
        - ln "source" "destination" 
            - if source is deleted the data still available  

## chain commands 
    - we can chain commands using ; 
        - echo  "hi" ; ls ; echo "there" 
            - this would execute the three commands ans if anyone failed it does not effect the other commands 

## info about the OS
- lsb_release -a:
    - to get the version of the OS 

- hostname
    - to see the name of the system 

- uname -a 
    - information about the kernel 

- uptime
    - since when the system is active 


## IDE to write files:
    - nano:
        - it is the easiest to create and write the files 

    - vi:
        - i     -> insert mode 
        - ESC   -> command mode
        - :wq!  -> write and exit 
        - :q!   -> exit without saving 
        - d     -> delete the line 
        - x     -> delete word 

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

    - chown -R user:group folder  
        - chown ese:ese /temp/test
        - to change the owner 
        - can be done only by the root 
        - -R to make it recursively 

    - chmod ug=rwx,o+x
        - chmod ug=rwx, o=r /temp/test 
        - to change the permissions
        - owner and the root can change permissions 

- users:
    - users:
        - would list all users in this system 

    - groups:
        - list all groups in the system

    - id username 
        - would show the groups which this id belongs to 
    
    - useradd -m "username" -G sudo -s /bin/bash 
        - would add the user and create home directory to it and add it to sudo group and user bash as shell

    - userdel -r user 
        - would delete this user and home directory

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

## systemctl:
    - we use it to manage daemon in systemd 
    - systemd is the init process 

    - systemctl start/stop/enable/disable/restart service 


## ps & top 
    - ps aux
        - would show the active process on the system 

    - top 
        - would show real time active process and we go to inactive terminal mode
        - q -> to quit 
        - k -> to kill process 

## crontab 
    - crontab -e 
        - to edit crontab 

## shutdown 
    - shutdown 
        - this would stop the system 

    - reboot
        - would restart the system

    - halt
        - stop the system right now 

## ssh
- to login 
- ssh -i path_of_key username@ip

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
