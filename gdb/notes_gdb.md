- to add symbol table to the code:
    - target_compile_options(${TARGET_NAME} 
    PUBLIC
    -g3 )

- to show the code:
    - list filename 

## commands
- start the debugging:
    - start 
- run the code normally:
    - run r

- to continue:
    - continue   c

- next step:
    - next       n

- to go in the function:
    - step s

- to add break point:
    - b file:line 

- to add breakpoint with condition 
    - b file:line if x==12

- to remove the breakpoint:
    - d index  

- to enable/disable breakpoint:
    - enable / disable index 

- to show the breakpoints:
    - info b

- to break at variable change:
    - watch variable name 

- to invoke function:
    - call function_name()

- to see always a variable:
    - display variable name

- to end:
    - finish     fin
    - quit

- to refresh:
    - refresh