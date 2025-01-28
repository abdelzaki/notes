- to install cmake:
    - sudo apt install cmake 
- the name of the cmake file 
    	- CMakeLists.txt  

- to decide the minimum version of cmake to use
    - cmake_minimum_required(VERSION 3.16)

- project("name of project")
    - would set the variable ${PROJECT_NAME}

- to generate executable:
    - add_executable("name of the binary" "files we need to build")

- to generate lib:
    - add_library(lib_name files_to_compile )

- to add files which is needed to be compiled:
    - target_sources(${TARGET_NAME}
    PRIVATE
        ${TARGET_NAME}.cpp
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/${TARGET_NAME}.hpp
    )

- to add the include directory where the compiler search for the header files:
    - target_include_directories("target_name" PUBLIC/PRIVATE folder )

- to link library 
    - target_link_libraries("target" library)

- if we want to add a path where find_package/find_library/find_path/find_program would also use to search for packages 
    - set(CMAKE_PREFIX_PATH "path")


- to assign variable:
    - set("name" value)
    - cmake -DvariableName=value 
    - option(value "comment" value)
        - this would store the value in cache CmakeCache.txt

- to show the variable value:
    - message(STATUS "message to print  ${variablename})

- to add another cmake file 
    - add_subdirectory(${CMAKE_SOURCE_DIR}/folder2 )

- to configure the compiler option:
    - target_compile_options(${TARGET_NAME}
        PRIVATE
            -Wall
            -Wextra
            -Wconversion
            -Wsign-conversion
             -g // for debugger
        )

- to configure the compiler definition :
    - target_compile_definitions (${TARGET_NAME}
        PUBLIC 
            APP_NAME="my_app" 
        )


- to copy files but we have to run the install command:
    - install(FILES source DESTIONATION folder)
    - cmake install path_to_build

- variables:
    - to get the path to the first cmake:
        - ${CMAKE_SOURCE_DIR}
    - to get the path of the current cmake:
        - ${CMAKE_CURRENT_LIST_DIR}
            - would get the source where i wrote it 
        - ${CMAKE_CURRENT_SOURCE_DIR}
            - the same but when we use include it would show the file where we was include written
        - ${CMAKE_BINARY_DIR}
            - point to the build folder

- run cmake:
    - make a directory build 
    - to create a make file:
        - cmake -S "path of the cmake" -B "where to build"
    
    - to build:
        - cmake --build "path of build folder" 

- to enable debug:
    - set(CMAKE_CXX_FLAGS "-g")

## unit test 
- mock:
    - 


## googletest
- to install googletest 
    - sudo apt install libgtest-dev
    - sudo apt install libmock-dev
    - this would install in /lib

- cmake in gtest:
    - find_package(GTest REQUIRED)
    
    - target_link_libraries(${target_name} 
        GTest::gtest
        GTest::gmock_main)
    
    - include(GoogleTest)
    
    - gtest_discover_tests(${target_name})