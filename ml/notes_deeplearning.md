# general 
    - aritifical intelligence -> machine linear [ML] -> deep learning 

## machine learning 
    - what is machine learning:
        - we have a computer which learns from the data  
        - computer which have the ability to learn with being explicity programmed 

    - supervised:
        - we teach the machine what to do 
        - we pass the data with a label which represents the solution 
        - ex:   
            - line regression [predict the price of a house based on some features] [continous result] 
            - classification [discret result]

    - unsupervided:
        - the macheine gets the pattern by itself 

    - reinforcement:
        - agent train in enviromental and learn by itself 
        - via reward and punishment the agent learn how to handle the issue  

## terminology 
    - training dataset 
        - the data we use to teach the model 

    - feature:
        - it is the input variabel 

    - traget:
        - it is the output variable 

    - m:
        - number of training sets

    - (x^(i) ,y^(i))
        - referes to the input / output variable 

    - y-hat is the prediction of the model 

## cost function 
    - it tells us how badly our system behaive 
    - we refer to it as J function
    - ex:
        - squirel error function 

## contour figure:
    - elipse which show the the parameter which have the same error values 


## gradient descent
    - it is a way to find the parameter which best fit to the line which represent the data 
    - it is a minize function
    - we have more than deep point of the cost function 
    - we reach the bottom with a little step which is different according to the start point 
    - algo:
        - w = w_old - α 'd/dw'j(w,b)
        - b = b_old - α 'd/dw'j(w,b)   

        - α:
            - it is the learning rate 
            - big α means we learn fast with a big step 

        - we update w and b at the same time 

## supervised
    -  regression
        - fit the data 
        - we expect the value of the house according to the size of the house
        - output is contououse values 

        - model:
            - single features:
                - we call it linear regressuin 
                - f = a + bx 
            
            - multiple features 
                - f = W1X1 + W2X2 + .. + b 
                - 

    - classification
        - output is catogorize 
        - output is limit number of results 
        - we expect if the image has a human or not  

        - logistic regression
            - sigmoid function 
                - it is a function which y goes from 0 .. 1 where at 0 y equal 0.5 
                y = 1 / 1 + e^-x 

            - decidion boundaries:
                - decide where to draw the line / shape to seperate between the data   

## unsupervised 
    - we donot have a label for the output data  
    - model should cluster the data by itself and find the pattern 
    - the different to classification is that we dont tell the model that 
    - ex:
        - anomaly finding

## features scaling  
    - we need to scale the features to make it faster to be calculated 
    - if the feature has a huge value a small change in the cofficient would make a big difference 

# neuteral networking 
    - we use here deep learning 
    - it has a deep layer 

    - neuron:
        - we have a series of input 
        - they are connected to weights     

    - activation functions:
        - sigmoid:
            - map the input between 0..1 

## training a neueral network 




    

## general 
- image has three colors [RGB]

## binary classification 
    - we have an input and say there is a cat or not  

## sound 
    - periodic 
        - simple
            - sine wave 

        - complex 
            - multiple sinewave 

    - aperiodic 
        - continous 
            - noise 

## audio and signaling 
    - higher frequency => higher pitch 
    - higher amplitude => louder  

    - ADC:
        - analog digital convertion 
        - sampeling and quantised 
        - sampling is a step 
        - quantised ist the step in the amplitude

## fourier:
    - general
        - we are interested in the amplitude as it shows how much this signal contribute to signal 
        - we get the magnitude as a function in frequency
        - we move from the time domain to the frequency domain 
        - no time information 

    - short time fourier:
        - computes serveral fft at different tome  
