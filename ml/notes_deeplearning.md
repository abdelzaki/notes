# general 
    - aritifical intelligence -> machine linear [ML] -> deep learning 

## machine learning 
    - what is machine learning:
        - we have a computer which learns from the data  
        - computer which have the ability to learn without being explicity programmed 
        - we have data and labels and the machine figure out the rules 

    - supervised:
        - we teach the machine what to do 
        - we pass the data with a label which represents the solution 
        - machine figures out the rule
        - ex:   
            - line regression [predict the price of a house based on some features] [continous result] 
            - classification [discret result]

    - unsupervided:
        - the macheine gets the pattern by itself
        - we have only the features without the label 
        - clustering the data 

    - reinforcement:
        - agent train in enviromental and learn by itself 
        - via reward and punishment the agent learn how to handle the issue  

## terminology 
    - training dataset 
        - the data we use to teach the model 

    - feature:
        - it is the input variabel 

    - traget:
    - label:
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

## vonvex
    - it is the function which has minimum deep point 

## fitting 
    - overfitting 
        - the model is adjust too much to fit the training data so the model captures also the noise in the data 

    - underfitting 
        - training data is not enough 
        - we choiced the wrong model to represent our system 

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
                - we call it linear regression 
                - f = a + bx 
            
            - multiple features 
                - f = W1X1 + W2X2 + .. + b 
                -  

            - polynomial regression 
                - f = w1x + w2x^2 + w3x^3 + b

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

## logistic regression
    - general:
        - we habve Nx features and we want to decide the output Y which ist binary{1,0}
        - we use sigmoid function to make the prediction value from 0 -> 1 
    
    - loss function 
        - it is the error function
        - we want to measure how good our prdiction is 
        - if we used the sameone like the linear regression we would get not convex function which it is hard to get the local minimum 
        - equation = -(ylog(y-hat) + (1-y)log(1-y))

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
    - data is reprenseted as data layer
    - it has a deep layer 

    - neuron:
        - we have a series of input 
        - they are connected to weights     

    - activation functions:
        - sigmoid:
            - map the input between 0..1 

## bias and variance 
    - bias:
        - the erro in the training set is to high 

    - variance:
        - different between training and testing is to high 

## training a neueral network 
### definition
    - iteration:
        - everytime the network update the weights 
        - everytime we make prediction 

    - epoch:
        - one epoch when the network has seen the whole dataset 

    - batchsize:
        - how many data we use to update the weights 

    - hyperparameter:
        - learning rate 
        - iteration 
        - number of hidden layers 
        - hidden neueron 
        - activation functions 
        


# - Convolutional Neural Networks [CNN]
    - we use it to detect image 

## convolution 
    - it has a kernel 
        - it is a feature detection 
        - we can extract features from the image using the kernel 

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
        - quantised ist the step in the y-axis

## fourier:
    - general
        - we are interested in the amplitude as it shows how much this signal contribute to signal 
        - we get the magnitude as a function in frequency
        - we move from the time domain to the frequency domain 
        - no time information 
        - we get amplitude which affect the signal through the whole time 

    - short time fourier:
        - computes serveral fft at different time
        - information about amplitude, frequency and time   
