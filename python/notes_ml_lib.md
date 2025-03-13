# juypter 
    - to run juypter 
        - start the juypter server 
            - jupyter lab 
        - to access it from the browser 
            - http://localhost:8888/lab

# pandas 
## generals
    - we use it to read csv files 
    - we can access row and columns 
    - we use it to analysis data 
    - to install pandas 
        - pip install pandasdf

    - to read csv file  
        - pd.read_csv("path_to_csv") 

    - dataframe 
        - it is a dictionary which has list as it's values 

    - to get all the coulumns 
        - df.columns

    - to get information about the data frame 
        - df.shape

    - access row:
        - to acess row by index
            - df.iloc[0] 

        - to access more than one row   
            - df.iloc[[0,1]]  

        - to access range 
            - df.iloc[0:2]

        - to access row using label
            - df.set_index("index_name, inplace=True) 
            - df.loc["index_name"] 

    - to set / reset index
        - df.set_index("name_of_index",inplace=True)
        - df.rest_index("name_of_index",inplace=True) 

    - to set how much data can we see 
        - pd.set_option("display.max_columns",110)
        - pd.set_option("display.max_rows",110)

    - access column
        - df["name_of_columns"] 

    - access first columns  
        - df.head()

    - to get statics
        - df.describe() 

    - to get statics of a certain columns 
        - df.['clolumns_name'].value_counts()

    
# matplotlib
## general
    - we use it to draw data
    - pip install matplotlib 
    - from matplotlib import pyplot as plt 

    - plot diagram 
        - to show a diagram 
            - plt.plot(list_x, list_y, label="str")
            - we can define the x and y labels 
                - plit.xlabel("")
                - plit.ylabel("")
                - plit.title("") 

        - to add legend which show the name of the curve 
            - plt.legend()

        - to add grid 
            - plt.grid(true)

        - draw the plot
            - plot.show() 

    - bar diagram
        - to show the data as bar 
            - plt.bar(list_x, list_y, label="str")

        - to show more than one bar 
            - change x axis to use numpy
                - x_index = np.arrange(len(our_list))

            - move the bar by this width 
                - width = .25
                - plt.bar(x_index - width, list_y, label="str")
                - plt.bar(x_index - width, list_y, label="str") 

            - adjust x axis values 
                - plt.xticks(ticks=x_index, labels=our_list)

# numpy 
    - it is numerical python library 
    - we can use it to multiple arrays 

    - numpy array
        - we save data with the same type 
        - it has fixed size 

    - create array 
        - normal way
            - np.array([[],[]])

        - array of zero 
            - np.zeros(shape = (3,5),dtype='int64')

        - sequal array 
            - array from 0 to 9 
            - np.arange(10) 

        - we can create using random numbers 


    - to get information
        - arr.size 
            - how many elements the array habe 
        
        - arr.dtype 
            - data type of the array 
        
        - array.shape 
            - the dimension of the array 

        - arr.ndim  
            - get number of dimension of the array

    - operations 
        - to perform dot operation which is multiple every element and sum the result 
            - result = np.dot(array1, array2) 


        - to perform array multiplication 
            - array3 = np.matmul(array1, array2) 
            - result = array1 @ array2 

        - element wise operations
            - array3 = array1 + array2
            - array3 = array1 * array2 


        - to add the same value to the whole array 
        - this would all 5 to evey element in this array
            - array2 = array1 + 5 

        - add all elements of the array 
            - arr.sum()

    - broadcasting 
        - operation between array of different sizes 
        - shape should be compitable means they habve the same number of element in the axis or the axis has size 1 
        - ex:
            - (3,) + (2 ,1) -> (2,3)


    - to read a csv fole
        - data = np.genfromtxt("path",delimiter=",", skip_header = 1)

    