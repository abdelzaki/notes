# Descriptive Statistics Basics
    - cases 
        - it is what we study 

    - variables
        - it is the features  

    - level of measurements
        - categorical 
            - nominal 
                - difference values
                - no order 

            - ordinal
                - difference value 
                - ordered

        - qunatitative    
            - interval
                - difference 
                - order 
                - similar interval 
                - no meaningful zero point

            - ratio
                - difference 
                - order 
                - similar interval 
                - meaningful zero point( void feature)

## vector 
    - i^ and j^ are the basis of xy coordinate system  
    - span:
        - it is the set of all their linear combinations 

## linear transformation 
    - all lines are parellel 
    - the origin remains 
    - we change the basis vector 
    - transformation
        [1_i^ 1_j^]
        [2_i^ 2_j^]


## matrix   
    - defination
        - array of numerbs arranged into Rows and columns 
        - size is row * columns 
        - up/down is row 
        - right/leght is columns 

    - adding / substraction 
        - matrix should be the same size  
    
    - scalar
        - we multiple the matrix with a constant  

    - multiplication:
        - it is moving the whole system with the matrix we multiple 

## determint
    - the factor by which the area increased / decreased
    - how much the area change by the transformation 

## augmented matrix
    - definition
        - we have function 4x -y + 2z = 7 
        - we write the coffient in a matrix and the result in a matrix 

    - elementary operations 
        - interchange
            - we can swap any colums    

    - scaling
        - we can multile any row with a constant 

    - replacement 
        - we can add any two rows and replace one of them with the result 

## reduced Row echelon Form 
    - equation:
        - 3x + 2y -4z - 12w = 12
    
    - case 1
        -   [1 0 0 0 | 3] 
            [0 1 0 0 | 5] 
            [0 0 1 0 | 9] 
            [0 0 0 1 | 1] 
            
        - this solution means the system is independent and it has only 1 unique solution 
    
    - case 2
        -   [1 0 0 0 | 3] 
            [0 1 0 0 | 5] 
            [0 0 1 0 | 9] 
            [0 0 0 0 | 1] 
        
        - this system has no solution 

    - case 3
        -   [1 0 0 0 | 3] 
            [0 1 0 0 | 5] 
            [0 0 1 0 | 9] 
            [0 0 0 0 | 0] 
        
        - this system has infinite solutions as it has more variable then the leadings 1 

# calculus