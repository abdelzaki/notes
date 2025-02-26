## mysql 
    - it is open source database 
    - it is the engine which we use to perform database 
    - it is owned by oracle 
    - it has some forks 
        - mariadb 
        - enterprise edition  

    - mysql-server
        - it is the package of mysql  

    - to access mysql
        - mysql -u "username" -pPassword 

    - to see the databases 
        - show databases;

    - to know where the data is stored in mysql
        - show variables where variable_name='datadir';

    - to create database 
        - CREATE DATABASE testdb; 

    - to create table inside database 
        -   USE testdb;
            CREATE TABLE tbl1 (id INT, name VARCHAR(20));
            exit; 

    - to switch to a specific database
        - use name_of_db 

## design 
    - we start with superset (table which has all attributes) 
    - then we seperate the table in small tables and relate tables with each other 

## keys
    - it a column or group of columns 
    - it has a unique value  

    - primary key:
        - it is the key which has the least amount of column which is uniques 

    - foreign key:
        - it is a key in this table which is a primary key in another table 

## relational database 
    - it is represented as a table 
    - row = record = relation 
    - colum = field = attribute 
    - entity = table 

## mysql workbench 
    - it has by default 3000 

## sql 
    - it is executed in the database 
    - it is declarative 
    -  DML:
        - data manupliation 
## select 
    - select 'ahmed' like 'ahmed'
        - compare two string 

    - select "ahmed, me" LIKE "hello, %" 
        - % it is wildcard
        - %aa% -> word contain aa 

        - 


        - insert 
        - update
        - delete 
        - merge
        - upsert


    


