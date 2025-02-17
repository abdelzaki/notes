## shell
    - shell is interpreter which pass command to the OS[kernel]
    - types of shell such as bash or sh  

## terminal
    - it is a way to communicate with the shell 
    - terminal could be sh or bash 
    - #!/bin/sh
    - #!/bin/bash

### prompt 
    - username@machine_name
    - # -> root 
    - $ -> normal user 

## tty 
    - we can log with more than one user we can use tty 
    - tty 
        - would show us which tty we are currently using 

## change user 
    - change users:
        	- the '-'
                - means change the working directoy to the home directoy of this user  

        - su - username 
            - change to this user 
            - go to the home directoy of this user 
        - su - 
            - change to root 
            - go to the home directroy of the root 
            - we are in /root 

        - su 
            - change to root 
            - stay in this directory

    - root can change to any user without password 

    - exit
        - this command we exit the active session and go to the next session 
        - if this is the last session it would close the terminal 

## change the password 
    - passwd 
        - this would change my own password 

    - sudo passwd user_name
        - this would change the password of this user 

    - sudo passwd 
        - this would change the password of the sudo user   

## sudo 
    - if the user is joined to the sudo group can perform super command 
    - sudo command 
        - here would ask password of the current user 

    sudo -i
        - ask for my password 
        - perform super commands

## file system 
    - file system starts from the the directory / 
    
    - /home
        - the home directory of all users 
    
    - /root 
        - home directory of root user 

    - /bin 
        - commands whould be here written 
        - it is link to /usr/bin

    - /sbin 
        - commands of the root user 
        - it is link to usr/sbin

    - /etc 
        - configuration file 
    
    - /opt 
        - third party applications 

    - /proc 
        - information about process 

### link 
    - soft_link means if the original file deleted the link points to nothing and we cannot read the data anymore 
        - link -s "source" destination 
            - this would create soft link, if the source deleted the link is not valid 

    - hard_link if the source is deleted the hard_link still has the data 
        - ln "source" "destination" 
            - if source is deleted the data still available  

## naviagation 
    - ~
        - this show home directoy of the current user 

    - ls 
        - list directory and file 
    
    - cd -
        - go back to the last directory i was in 
    
## copy and create
    - to copy a file or folder  
        - cp -r source destination     
        - cp -r folder1 ../folder2 
            - this would move the folder to the parent folder
                - if folder2 does not exist it would copy folder1 and rename it to folder2
                - if folder2 exists  it would copy folder1 inside it and the folder would still have the same name 

        - cp -r folder1 ../folder2 
            - if folder2 does not exist it would move the folder 

## find 
    - find path -name "name"
        - sudo find / -name "sps" 
            - this would search the file sps in the whole system 

## info about the OS
- lsb_release -a:
    - to get the version of the OS 

- hostname
    - to see the name of the system 

- uname -a 
    - information about the kernel 

- uptime
    - since when the system is active 

## compressing 
    - applied to file
    - gzip file_name
        - would compress the file  

    - gzip -d file_name
        - would unzip the file 

## archiving 
    - applied to folder
    - create folder.tar
    - tar -command filename.tar origin_data
        - -cf :create archive 
        - -xf : extract
        - -tf : list files 
        - -vf : verbose 
        - z   : archieve and compress
        - we use sudo tar -c so we can keep the previous owner 


## IDE to write files:
    - nano:
        - it is the easiest to create and write the files 

    - vi:
        - i     -> insert mode 
        - o     -> insert new line
        - ESC   -> command mode
        - v     -> visual
        - :wq!  -> write and exit 
        - :q!   -> exit without saving 
        - d     -> delete the line 
        - dw    -> delete line 
        - x     -> delete word 
        - dw    -> delete till the end of the line
        - u     -> undo
        - set number -> show line number 
        - w newfile -> write to another file 

## permissions:
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
        - a refere to all
        - chmod +x -> excute for everyone
        - chmod ug=rwx, o=r /temp/test 
        - to change the permissions
        - owner and the root can change permissions 

## users:
    - systemusers 
        - it has id which is less than 999
        - process takes systemuser id 
        - systemuser can not open shell 

    - sudo users:
        - would list all users in this system 

    - groups:
        - list all groups in the system

    - id username 
        - would show the groups which this id belongs to 

    - id 
        - show information about me 
    
    - useradd -m "username" -G sudo -s /bin/bash 
        - args
            - -m
                - create home 

            - -s 
                - shell type 

            - -G 
                - group to join 

            - -c 
                - comment 

        - would add the user and create home directory to it and add it to sudo group and user bash as shell
        - then i should create password to this user  

    - userdel -r user 
        - would delete this user and home directory

    - usermod user
        - would change the user  
        - -aG group1,group2
            - would add the user to this group 
        
        - -rG group1 
            - remove the user from this group 

    - /etc/passwd
        - information about the users in the system 
        - username:password[x]:userid:groupid:comment:home_directoy:default_shell 

    - /etc/shadow 
        - here is the password of the users encrypted
        - user_name:password:days_from_epoc:minimum_days_to_change_password:minimun_days_to_change_password
         warning_before_expiration: 

## process
    - anything which can run 
    
    - to run process in the background & 
        - command & 
    
    - to end a process:
        - kill pid 
        - kill -9 pid -> this cannot be caught 
        - pkill name
    
    - ps
        - show process which is running in this terminal 
        - -a 
            - show all process on all termianl
    - ps aux
        - show all the process 
        - a 
            - all terminal 

        - u 
            - more information 

        - x 
            - show process which is started by the kernel 

    - ps -ef
        - would show the parent and children of the process  

    - top 
        - would show real time active process and we go to inactive terminal mode
        - q -> to quit 
        - k -> to kill process 

## systemctl:
    - we use it to manage daemon in systemd 
    - systemd is the init process 

    - systemctl start/stop/enable/disable/restart service 

## crontab 
    - crontab -e 
        - to edit crontab 
    
    - days of week:
        - 0 and 7 is sunday
        - 1 monday

    - */5 -> every 5 minutes 

## shutdown 
    - shutdown 
        - this would stop the system 

    - reboot
        - would restart the system

    - halt
        - stop the system right now 

## networking 
    - ip link show
        - would show us the internet cards 

        - link/ether
            - that is the mac address 

    - ifconfig
        - it is an old command
        - it is a package inside net-tools
        - would show us the ip address
        - inet
            - it is the ip address     

    - ip address show
        - it is the new way to show the ip-address      

    - ip route 
        - show as the routing table   

    - nmcli 
        - network manangement command line interface 
        - nmcli device status 
        - connection:
            - is the configuration 
        - device:
            - is the hardware

        - configuration is saved in /etc/NetworkManager/system-connections 

    - to change hostname:
        - hostnamectl set

## ssh
    - package name openssh-server this would install sshd
    - we have two keys public and private 
    - default port is 22 
    
    - to login 
        - ssh -i path_of_key username@ip 

    - to generate key 
        - ssh-keygen 
            - this would generate public and private key which 
        
        - ssh-copy-id user@ip
            - to copy the public key 


### simple commands
    - command options argument


    - we can chain commands using ; 
        - echo  "hi" ; ls ; echo "there" 
            - this would execute the three commands ans if anyone failed it does not effect the other commands 
    - date
        - show the date 

    - cal 
        - would show us the calender 
        - cal 2022
            - would show us the calender of the year 2022

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
