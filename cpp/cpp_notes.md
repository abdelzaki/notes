- header file:
    - header files from c are still available but without the extension .h and with suffix c example <cstdio> here every thing is inside std name space 

- preprocessor:
    - #define key value 
    - #pragma once 


- operator:
    - bit operators
        - & 
            - bitwise and 
        
        - | 
            - bitwise or  
        
        - && 
            - logical and 

        - || 
            - logical or 

        - logical and , logical or both uses short circuit operations 

- namespace:
    - in cpp file you can define namespace in two ways
        - option 1:
            namespace my_namespace{
                void my_function(){}
            }
        
        - option 2:
            - void my_namespace::my_function(){} 

    - we can leave out the namespace when we call the function when we using "using namespace --" keyword
        - using namespace my_namespace;

- literal:
    - it is used to write numbers or string 
    - examples:
        - decimal:
            - 12 

        - hex:
            - 0x12 

        - binary:
            - 0b0102

- predefined variable:
    - __func__:
        - this would return the function name    

- casting:
    - static cast 
    - int i3  = static_cast<int>(i2)


- enum:
    - normal enum
        - to define enum:
            - enum my_enum {white, blow, yellow}
            - my_enum enum_1 = 0;
    
    - enum class
        - enum class my_enum_class{white, yellow, green}
        - my_enum_class enum_2 = my_enum_class::white 

- initializer list:
    - auto x = {1} // initializer list 
    - auto x = {1,2} // initializer list 
    - auto x {1} // integer 
    - auto x {1,2} // error

- string:
    - c style string 
        - header file is <cstring>
        - it is an array with char where the last char is "\0"
        - strlen() would return the size of a string not the size + the "\0" 
        - sizeof() return the size of the data type 
            - char str1[] = "ss"
                - sizeof would return the length + the "\0"
                - we can modify them as it is an array
            - char str2* = "ss" 
                - would return the size of a pointer
                - we cannot modify them as it is an const char* str ="ss"

    - raw string literal: 
        - const char* str = R"(string which we need )"

    - auto with string:
        - auto str = "-" -> would de const char*
        - auto str = "-"s -> would be std::string 

    - string view:
        - it is used when you want to define function with accept std::string and const char * 
        - you can convert implicit string view to string you have to call data or to use std::string constructor 

- pointer:
        - header file ist <memory>
    - unique_ptr:
        - auto var = std::make_unique<type>();
        - std_unique_ptr<type> var(raw_pointer)

        - get():
            - would return the raw pointer 

        - reset():
            - would delete the raw pointer and assign the smart pointer to NULL 

        - release():
            - would return the raw pointer and assign the smart pointer to null, the raw pointer still exists 
    
    - shared memory:
        - the destructor is called when the reference counting is null 

    - shared_from_this:
        - the class has to inheritance from enable_shared_from_this 
        - return shared_from_this would always return the same object not a new object 

- default parameter:
    - we can assign default parameter to a function in the header file
    - we assign default value of the member of the class in the hpp file

- class:
    - initialize the member in the hpp file 

- static:
    - static member:
        - one instance of the member in the whole program 
        - we have to initialize it in the cpp file or to write inline in the hpp file 

    - const static member:
        - we cannot reassign them 
        - we can initialize them in the hpp without inline keyword 

- override:
    - it allows base class reference / pointer to access derived class method 
    - destructor should be always virtual if u called delete on a base class pointer to derived the base destructor would
    be called

- inheritance
        