- header file:
    - header files from c are still available but without the extension .h and with suffix c example <cstdio> here every thing is inside std name space 

- preprocessor:
    - #define key value 
    - #pragma once 

- main:
    - it is the start point of the program 
    - return 0 if the program ended without failure 
    - non zero return means a failure has happened  

- macro:
    - always put the ars inside ()
    - example:
        - #define double(x) ((x) * x)*
        - double (1+2) would be replaced with ((1+2)*(1+2))

- types:
    - bool:
        - 0 and 1 

    - char:
        - 'a'

    - int:
        - 1,2,3 

    - double:
        - 1.2

    - size_t:
        - it is typdef of unsigned number 

- asci:
    - 7 bits to represent char 
    - it is printable 
    - american standard 

- unicode:
    - 4 bytes 
    - represent more chars 

- utf-8:
    - length it adjustable for each chars 

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

    - unname namespace:
        - if we want to link a function / variable  locally we define it in a name space this why only this file can access this definition

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

- include c code in c++:
    - extern "C" {}
    - this would tell the compiler that this functions are written in c, so the linker can find them when he trys to call them.

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
        - std::unique_ptr<type> var(raw_ptr)
        - never create two smart pointer from the same raw pointer, this would led that the delete is called twice 
            - std_unique_ptr<type> var_1(raw_pointer)
            - std_unique_ptr<type> var_2(raw_pointer) -> delete is called here twice 

        - get():
            - would return the raw pointer 

        - reset():
            - would delete the raw pointer and assign the smart pointer to NULL 
            - we can use it to reassign smart pointer 
                - std::unique_ptr<type>var;
                - var.reset(new type())

        - release():
            - would return the raw pointer and assign the smart pointer to null, the raw pointer still exists 
    
    - shared memory:
        - the destructor is called when the reference counting is null 
        - data race happens if we try to access the data from different threads 

    - shared_from_this:
        - we cannot call it in the constructor, this is very important 
        - the class has to inheritance from enable_shared_from_this<type>
        - return shared_from_this would always return the same object not a new object 
        - Note that you can only use shared_from_this() on an object if its pointer has already been
            stored in a shared_ptr.
        - if we pass "this" to asynchronous function the object wont be deleted until the asynchronous function is over 

    - weak_from_this:
        - if the class wants to have a reference to itself which maybe would pass to callback function 
        - we can use lock to get shared pointer from weak pointer

- chrono:
    - header file <chrono>
    - it is the number of ticks of a specific unit of seconds 
    - std::chrono::duration<int,std::ratio<60>> two_minutes(2)
    - std::chrono::seconds threeSeconds(3)
    - we can convert bigger time unit to small without casting (minutes to seconds) 

- clock:
    - steady_clock:
        - it is never adjusted means the time_point would never be minus 

    - chrono::system_clock::now()
        - would get the current time 

- default parameter:
    - we can assign default parameter to a function in the header file
    - we assign default value of the member of the class in the hpp file

- function object:
    - object which has the operator ()

- class:
    - initialize the member in the hpp file 

- static:
    - static member:
        - one instance of the member in the whole program 
        - we have to initialize it in the cpp file or to write inline in the hpp file 

    - const static member:
        - we cannot reassign them 
        - we can initialize them in the hpp without inline keyword 
    
- static_assert(bool, message):
    - this can help us to find the error at compile time

    
- type alias:
    - using name = const int*

- inheritance:
    - override:
        - it allows base class reference / pointer to access derived class method 
        - we can override public, private, protected methods
        - destructor should be always virtual if u called delete on a base class pointer to derived the base destructor would
        be called

        - we can only override method with the same prototype the only exception is if the return type is different 
        but it is a raw pointer see the example in professional c++ 

    - hidden method:
        - method in the derived class with different parameter. then the derived object cannot call the base method 
        - if u want to use the base method and the derived method "using base_class::base_method"

    - static:
        - we cannot override a static method 
        - static method is called by class name that why both base and derived class can have the same method_name
        

- standard utility:
    - std::bind:
        - we can bind a function with parameter 
    - vector:
        - header file is <vector>
        - [] -> does not provide boundary check 
        - at -> provides boundary check an throw out_of_range 
        constructor:
            - std::vector<int> vec1; 
            - std::vector<int> vec1(10,200)
            - std::vector<int> vec1({1,2,3})

        - assign():
            - would delete the old values and assign new values to the vector 

        vector of references: 
        - vector<reference_wrapper<string>> vec;
        - vec.push_back(ref(x))
        
        - size():
            - to get the size of the vector

        - reserve(int):
            - would reserve memory for x elements

        - empty()
            - return weather the size of the vector = 0

        - front():
            - get the first element 

        - back():
            - get the last element 
        
        - clear():
            - remove all elements of the vector 

        - erase(iterator):
            - delete the element


    - deque:
        - it is the same as vector but the elements are added at both end 

    - set:
        - sort elements according to a certain criterion 
        - type in set must be comparable 

- algo:
    - find:
        - return operator if the element if find in a container 

    - find_if:
        - it return iterator and the comparison are done on a lambda 
        - auto it = find_if(cbegin(myVector), endIt, [](int i){ return i >= 100; });

    - std::function:
        - we can use it to store a function 

    - lambda:
        - [=] captures all variables by value
        - [&] captures all variables by reference
        - [this] captures the current object it is a pointer so we can change the original object
        - [*this] captures a copy of the current object
        - if we capture by value we get the value of the parameter when we define the lambda but we capture by reference we get 
            the value of the parameter when we called the lambda 

- operator # amd ##:
    - To create a string from an identifier using the preprocessor's operator#, use the following pattern:
        - #define MAKE_STR2(x) #x
        - #define MAKE_STR(x) MAKE_STR2(x)

# template:
- function template:
    - definition
        - template <class T>
            T app_max (T a, T b) {
            return (a>b?a:b);}    

    - instantiation:
        - int x =  app_max<int>(3,5)
        - auto b = app_max(2,5)

    - Specialization:
        - template <>
            std::string app_max<std::string> (std::string a, std::string b){
            return (a[0]>b[0]?a:b); }

    - priority:
        - Perform overload resolution among regular functions and non-specialized templates.
        - If a non-specialized template is selected, check if a specialization exists that
            would be a better match for it.

- class template:
    - definition
        - template <class T>
        class V {
            T * m_buf;
        public:
            V( int n = 0) : m_nEle(n), m_buf(0) { creatBuf();}
            ~V(){ deleteBuf(); }
            V& operator = (const V &rhs) { /* ... */}}

    - instantiation:
        - V<char> cV;
        - V<int> iV(10);
        - V<float> fV(5);