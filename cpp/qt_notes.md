- Qobject:
    - it does not have a copy constructor 
    - we have object tree to manage memory 
    - when the father is deleted the children are deleted also 
    - we can the object name of qt object
    - it can have property added in the run time 
    - When an object is deleted, it emits a destroyed() signal
    - By default, a QObject lives in the thread in which it is created. An object's thread affinity can be queried using thread() and changed using moveToThread()
    
    - Member Function 
        - blockSignals:
            - this would block the signal of this object
            - if we emit the signal no thing would happen 



- view class:
    - this means it is read only class 
    - QByteview:
        - read only QByte

- Qlist: 
    - dynamic array so basically it is a vector 
    - append():
        - add element to the list 
    
    - remove():
        - remove the first occurrence of an element
    
    - removeAll():
        - remove all Occurrence of an element 

    - size():
        - number of elements 

    - contains():
        - true if element exists 

    - clear():
        - empty the list

- signals and slots:
    - they should have the same prototype  
    - we have to connect the signals with the slots 
    - signal can connect to many slots, one slot can be connected to many signals
    - If a signal is connected to several slots, the slots are activated in the same order in which the connections were made, when the signal is emitted.
    
    - signals:
        - it is the producer and it does not have an implementation 
        - it has to be called using emit signal()

    - connect:
        - we can connect signal and slot 
    
    - disconnect:
        - would remove the connection between signal and slot  

    
    - slot:
        - the consumer of a signal 
        - it has a definition and implementation 
        - it is like a call back function 

- threads:
    - header file is <QThread>
    - Qthread::currentThread()
        - would get the current running thread 