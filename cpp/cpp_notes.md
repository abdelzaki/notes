- header file:
    - header files from c are still available but without the extension .h and with suffix c example <cstdio> here every thing is inside std name space 

- preprocessor:
    - #define key value 
    - #pragma once 

- main:
    - it is the start point of the program 
    - return 0 if the program ended without failure 
    - non zero return means a failure has happened  

## macro
    - always put the ars inside ()
    - example:
        - #define double(x) ((x) * x)*
        - double (1+2) would be replaced with ((1+2)*(1+2))

## type alias
    - type alias for integer are found in <stdint> header file
    - using name = const int* 
    - typedef int uint32_t 
        - in our code we use uint32_t when we want to use 32bits if we ported the machine to another 
        machine where the int is not 32 bits we would change the typedef to long
        typedef ling uint32_t

## pointer 
- int* pi           -> pointer to an integer 
- int** ppi         -> double pointer to an integer 
- int* ap[15]       -> array of pointers to integer 
- int* f(char*)     -> function with takes pointer and return pointer 
- int* (*f)(char*)  -> function pointer to a function with take pointer and return pointer


### const and pointer
    - always read it from right to left 
    - if const is left to the * then the data is const 
    - const char *
    - char const *
        - both are pointer to constant means we cannot change the value but we can change the pointer to point to new thing 

    - char * const
        - const char pointer means we cannot change what the pointer is pointing to but we can change the value 

## types
    - bool:
        - true and false
        - any number which is not zero would be considered true
        - non null pointer is converted to true 

    - char:
        - 'a'
        - we can use +  and - on this characters the char would be changed to the
        the integer which matches this character and the operation is done.
        - '1' + 1 -> would result in 49 as '1' equals to 48
        - it is better to always use unsigned char 

    - int:
        - 1,2,3 
        - it is by default signed 

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

## namespace
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

    - inline namespace:
        - we use it to enable ABI[application binary interface] the compiler would add the namespace before our namespace when we call the function and when we have a new version we add the inline before the new version and then the compiler would call the new version automatically 

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

## auto 
- auto with initializer list would considered a list : 
    - auto x = {1} // initializer list 
    - auto x = {1,2} // initializer list 
    - auto x {1} // initializer list  
    - auto x {1,2} // error

- with = 
    - auto x = 1 -> integer 

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
        - c_str() would get c style string from a string which is a pointer to a string when the string is deallocated the pointer is valid any more that is very important 

        - to change any numbers to string we use std::to_string() which convert the number to string

    - raw string literal: 
        - const char* str = R"(string which we need )"

    - auto with string:
        - auto str = "-" -> would de const char*
        - auto str = "-"s -> would be std::string we have write "using namespace std::string_literals;"
        auto sv = "sdfc"sv -> would create string view, we have to write "using namespace std::string_view_literals;"

    - string view:
        - it is used when you want to define function with accept const std::string& and const char * 
        - you can convert implicit string view to string. you have to call data or to use std::string constructor 

## pointer
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

## pair 
    - The class pair treats two values as a single unit
    - Piecewise Construction 
        - it is used to decay the elements of the two tuples which are passed to create the
        element of the pair 
    - std::make_pair(12,"my_name"s) -> would create pair of int and string 
    - access the element using first and second attribute 

## tuples
    - class that has an arbitrary number of elements 
    - we can use make_tuple to create tuple without the need to define the types of the elements 

## variant 
    - std::variant it is the modern way to implement union 
    - we can declare different data types in variant and reassign the variable according to the datatype 
    ex:
        - std::variant<int,bool,float> var_1
        - var_1 = 5 
        - auto x = std::get_if<int>(&var1)  
        - x now is a pointer to integer 

    - std::monostate as one of the types in a variant, 
    we allow the variant to be default-constructed in a valid state without holding any other types

## optional 
    - std::optional can have the data or std::null_ptr 
    - we can check it with if statement and access the data with the * operator

## bitsets

## chrono
    - using namespace std::chrono_literals; 
        - to use s and ms
    - header file <chrono>
    - duration it is the number of ticks of a specific unit of seconds 
    - std::chrono::duration<int,std::ratio<60>> two_minutes(2)
    - std::chrono::seconds threeSeconds(3)
    - we can convert bigger time unit to small without casting (minutes to seconds) 
    - .count() -> would return the number of ticks in the duration
    
- clock:
    - steady_clock:
        - it is never adjusted means the time_point would never be minus 

    - chrono::system_clock::now()
        - would get the current time 
    - to get the diff between two time points:
        auto now = std::chrono::system_clock::now(); // type is std::chrono::system_clock::time_point
        std::this_thread::sleep_for(1050ms);
        auto later = std::chrono::system_clock::now();
        auto duration = later - now;
        std::cout << std::chrono::duration_cast<std::chrono::seconds>(duration).count() << "\n";
        std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(duration).count() << "\n";
    
    
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

## inheritance
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

## container 
### sequential 
    - array
        - the size of the container doesnot change 
    
    - vector:
        - size grow in one direction 
    
    - deque:
        - size change in two directions 

    - list:
        - it is linked list 

### associative
    - map and set 

## vector 
    - header file is <vector>
    - dynamic array 
    - it has random access 
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

## deque
    - double ended queue 
    - it is the same as vector but the elements are added at both end 
    - we can add element the the begin using push_front()

## list 
    - it is linked list 
    - Lists do not provide random access
    - empty()
        - to check if the list has elements 

    - front()
        - would get the first element in the list 

    - pop_front()
        - remove the first element in the list 

## set
    - collection of elements with no duplication
    - sort elements according to a certain criterion 
    - type in set must be comparable 

## map
    - it is container of key value pair 
    - to find an element in the map 
        - auto iterator = map.find(key)
        - iterator.first return key 
        - iterator.second return value 
        - if the element doesnot exist it would return end()
    
    - to insert element 
        - map.insert({key,value})

    - to remove element by key 
        - map.erase(key)

    - to remove element by iterator 
        - auto it = map.find(key)
        - map.erase(it)

    - to remove element by iterator
        std::map<std::string,float> coll;
        for (auto pos = coll.begin(); pos != coll.end(); ) {
        if (pos->second == value) 
            pos = coll.erase(pos);
        else 
            ++pos;
        }

    - map[key] = value
        - if key doesnot exist a default constructor would create the value 
        - then a copy assign would assign  the value to this key 
        - this method is slow as it contain two steps 

    - map.at(key)
        - if key doesnot exit an exception would be thrown


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
## Multiple Template Parameters
    - template parameter
        - template<typename T>

    - Call parameters
        - T max (T a, T b)

## typename inside template 
- when we define variable inside template which depends on another template we have to use typename
    - ex:
        template <typename T>
        class MyClass {
        typename T::SubType * ptr;
        };
    - without typename subtype would be considered a static variable 

## this qualifier 
- if u inherits from a template and u want to call method of the parent class always use this-> to indicate that you are using the vase method not a method in the global scope 
    - ex 
    template <typename T>
        class Base {
        public:
            void exit();};

        template <typename T>
            class Derived : Base<T> {
            public:
            void foo() {
            exit(); // calls external exit() or error we have to use this->exit()
            }
        };

## where to write the template 
- we write the template in the hpp file because the compiler create the template for a specific parameter when it is called and if we write the implementation in the cpp file when the compiler want to 
create an instance of the template he cannot create it because the code is written in another file 

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

## design pattern 
### solid 
- single responsibility:
    - a function should do only one thing 
    - if a function has and in it is name means we war not obeying this rule 

- open closed:
    - open for extension closed for modification 

- liskov substitution principle:
    - if a function works with a pointer or reference to the base class it should also work with a pointer or a reference to all it is subclasses 

- interface segregation:
    - no client should be forced to depend on methods this it does not use 

- Dependency inversion principle:
    - high level modules should not depend on a lower level ones instead both 
    should depend on abstraction


dgdssafsafsdsdfasdffsdfsadf





safsadfsdf











