# usecase Model 
## actor
    - external entitiy
    - someone or something which plays a role regarding my system  
    - it should be outside the automation boundary

## automation boundary 
    - square shape which represents everything which can be automated 

## usecase
    - it is represented as oval shape
    - it is a complete action not a sub action

## include
    - means case A depends on Case B
    - ex: withdraw money includes login
    - arrow goes from Withdraw to login 

## extend
    - it is an optional 
    - the arrow goes from the optional to the mandoitary case 
    - it only happend if somethin happened which doesnot happen every time

## consideration:
    - we dont represent the sequence of the events 
    - two actors must not communicate with each other 

# sequence diagram 
- interaction between objects during a certain period of  time 

## dimension:
- right to left:
    - that is the object dimentions where the actors are listed 

- up to bottom:
    - there is where the time is listed 

## symbols
- thin rectagle on the lifeline of an object represent an activation of an object


# class diagram
## consist of:
    - Name: 
        - abstract class should be mutalic 
    
    - attribute 
        - width : int 
    
    - methods 
        - distance(r:int): double

- visibility:
    - +: public 
    - #: protected 
    - -: private 

## associational:
    - means relationship 
    - *: zero or many 
    - 1..*: one to many 
    - 1: one 

## diamond:
    - it is always the owner 

## aggregation:
    - symbolized with white diamond 
    - means it is part of 
    - example car has an engine
    - diamon would be at the car 

## composition:
    - symbolized with black diamond 
    - means it is made of this thing
    - example books is made of pages

## arrow:
    - arrow not empty means inheriate arrow at the base 
    - empty arrow means has[contain] arrow at the owner 

# component diagram
## interface 
    - )- : means required interface probably it is an input
    - circle: means optional interface probably an output 
