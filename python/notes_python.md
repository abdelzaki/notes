## string 
    - string in python is written using "" or '' 
    - """ we use this to write multiple line string """ 
    - .upper()
        - change the string to upper 

    - .cout("string_to_search")
        - count number of this string inside this string 

    - .find()
        - return index of the string 
        - -1 if we didnot find it 

## string formatting
    - " any thing {} with another anything {}".format(var1.var2)
    
    - any thing {0} with another anything {01} with any {0}".format(var1.var2)
        - we can use indexing to access the data 

    - " the value inside a dictionary {key_1}".format(**dictionary) 

    - f"hi there {var_1} iam {var_2}" 

## integer 
    - int("12")
        - would change string to integer 

## list
    - it is an array 
    - empty_list = list()
    - courses = ["english", "arabic", "german"]
    
    - len(coures)
        - show the size of the list 

    - courses[-1]
        - negtaive number access the element from the opposite direction 

    - courses[0:2]
        - slicing the list 
        - get the first two elements 

    - .append("new_element")
        - add element to the list 

    - .insert(index, element)
        - insert element in a specific location 

    - .extend(another_list)
        - append the element of the another_list to the origin list 

    - .pop()
        - remove the last element 

    - .index(element)
        - return the index of the element 
        - it would return error if the element is not in the list 

    - value in list 
        - return true if the element exists 
    
    - enumerate(courses)
        - return the index and the value of the list elements 
    
    - if we copy the list and changed the list would change both of them 

### list cpmprehensions
    - new_list = [n*n for n in old_list ] 
    - new_list = [n*n for n in old_list if n > 5 ]

## tuple 
    - we cannot modify it 
    - empty_tuple = tuple()
    - tuple = ("element_1", "element_2", "element_3")  

## nametuple 
    - it is like enum 
    - defined inside collections 

    - Color = namedtupled("name", ["red","white", "black"]) -> defined the name 
    - color = Color(1,3,5) -> define values 
    - x = color.white

## set 
    - it has unique elements 
    - empty_set = set()
    - courses = {"element_1", "element_2", "element_3"} 
    - it is unordered 
    - set_1.intersect(set_2)
        - would return set with the common elements 

## dictionary 
    - it is key value pair 
    
    - dict_1 = {"key" : value , "key_2" : 12} 
    
    - .get("key", "element_if_not_found)
        - return element if the key exists 
    
    - dict_1.pop(key)
        - remove the element from the dictionary and return it 

    - dict_1.key()
        - return all keys 

    - dict_1.values()
        - return all values 

    - dict_1.items()
        - return all the element 

### default dictionary 
    - from collections import defaultdict
    - we define the value type in declaration 
    - if we try to access the element which is not exit we wont get error but get default value of this value [int would return 0]

## slicing:
    - [start:end:step]
        - this is how we access the data
        - end is not included 

    - [0:index]
        - the index wont be included
        - means we get up to but not included index   

    - [0:1] 
        - would access only the first char 

    [-1]
        - get the last element

    
    [:-1]
        - get till the element before the last element 

## zip 
    - we can zip two list to a list with tuples 
    - so we can map the two items 
    - ex:
        - for x, y in zip(list1,list2)

## conditions 
    - and 
        - and condition 

    - or 
        - or condition 

    - not 
        - ! 

    - False 
        - emepty list, set, tuple, string , zero 

## iterations 
    - for x in list 
        - this would loop via the list 


## functions 
    - def function_name():
        pass 

    - def func(name, age = 12)
        - that is a function with a default value 

    - def func(*args, **kwargs)
        - this function take undefined numbers of parameter in args and name parameter in kwargs 
        - func( 1, 2 , name = "ahmed", age = 12)
            - args would have tuple with (1 ,2 )
            - kwargs have dictionary with {"name": "ahmed" , "age": 12} 

    - passing argument:
        - we can pass argument by poisition or by name
        - by positon should be alway at first 

    - poistion only parameter
        - def function_2(a= 10 , b= 20,/,c = 30 , d = 40 ):
        - before / parameter should only passed by position 
        - after / can be passed anyway
    
    - keyword only:
        - def function_2(a= 10 , b= 20,*,c = 30 , d = 40 ):  
        - c and d should be passed keyword only  

## import 
    - python search file in current folder, python standard library folder, package folder 

## closure and decorator 
### first class function 
    - function can be passed as a paraemter and be returned from a function 
    - we can return a function from another function and the returned function would remember the paraemter of the origin function 

### closure 
    - function remeber the variable which is defined outside it 
    - function capture the variable which is defined outside and also remember the parameter of the outter function

### decorator 
    - it take function as a parameter and execute it inside an internal function with is returned from the decorator
    - the decorator does not execute the inner function it return it 

    - @decorator 
        - this would take the function as a paramter and excute code before it 

    - we can make the decorator pass argument by using *args and **kwargs 

    - decorator itself can take arugments but defining outter decorator to the inner decotator 
    and call the decotaor @decotaor("arg_1")

## os  
    - module which allow us to work with operation system 

    - os.getchw()
        - show us the current working directory 

    - os.chdir(new_directory)
        - change the current working directory

    - os.listdir()
        - list all files and folder inside our current directory 

    - os.makedirs("tmp/val)
        - create directory 

## random 
    - get random number between 0 and 1 but 1 is not included 
    - value = random.random()
        - get number between 0 and 1 but 1 is not included

    - value = random.randint(1,6)
        - random integer between 1 and 6 this include 1 and 6 

    - value = random.choice(list)
        - it get a random value from this list  

    - value = random.choices(list, k=10)
        - this would return a list of 10 elements 

    - random.schuffle(list)
        - this would schuffle the list 

    - hand = random.sample(list, k=12)
        - this return a unique random element
        - choices method could return the same element twice 

## pip 
    - pip list  
        - list all pip installed which we installed 

    - pip install -r requirements.txt 
        - install all package which is listed here 



    
