## installation 
### to install in linux 
    - apt install -y libgtest-dev 
    - apt install -y libgmock-dev

### cmake 
- to enable c_test: 
    - enable_testing()

- to link against gest:
    - target_link_libraries(
            ${target}
            GTest::gtest
            GTest::gmock_main
        )

- gtest discover tests:
    - include(GoogleTest)
    - gtest_discover_tests(${target}) 

## methods
- TEST(suit_name, testcase_name)

## assertions 
    - EXPECT:
        - not fatal failure

    - ASSERT:
        - fatal failure

    - EXPECT_PRED2(): 
        - would give more information if the test case failed 
        - for functions which return Bool 

## disable 
    - if we want to disable a testcase we write DISABLED_ before the name of the testcase 

    - if we want to disable a group of testcase we write DISABLED_ before the name of the test suite 

## string 
- to work with string we use ASSERT_STREQ 

## subroutine 
    - if we want to use function which has assert more than one time in the testcase we write 
    { SCOPED_TRACE("message"); function_to_test(); } before this function. we would get this message when the testcase fail 

## data testcase 
    - we use it to test our testcase against different data set 
    - INSTANTIATE_TEST_CASE_P(uniqueeName,my_fixture,..)
        - name would tell us the dataset which we test against 
        - we test all testcases inside my_fixture against this data

## matchers
    - headerfile is "gmock/gmock.h" 
    - EXPECT_THAT(actual value, condition)
    - conditions:
        - StartsWith
        - AllOf(Gt(), Lt())
        - AnyOf() -> or 
        - Conditioal(cond, m1,m2)
            - cond = true -> m1 else m2 
        
        - Each
            - every element 
        
        Times(3)
            - number of time

        

## fixture 
    - testcase should be TEST_F(fixture, name_of_test_casw)
    - structure which inherhiate from publich testing::Test
    
    - SetUp and TearDown:   
        - would be executed every time each testcase runs 

    - SetUpTestSuite, TearDownTestSuite:
        - would be executed before the first Testcase in the Suite and the last Testcase in the suite 
    
    - member variable are accessed without the name scope of the fixture 
    - all member variable would be initialized before the Setup in the Fixture that is why we use pointer 

# gMock
## Mock 
    - allows us to check the interaction between itself and the code which is using it 
    - we use mock to mock an interface 
    - we test the component which use this interface not the interface itself 
    - destructor of the class should be virtual 
    - we test how many time a function has been called, and decide what should it return


    - class MyMock : public origin_class {
    public:
        MOCK_METHOD(ReturnType, MethodName, (Args...));
        MOCK_METHOD(ReturnType, MethodName, (Args...), (Specs...));};

## uninteresting call 
    - methods which we donot have any unexpected calls 

    - NiceMock<type>:
        - no uninteresting warnings would be shown if a method is called which 
        i have not defined 

    - StrickMock<Type>:
        - uninteresting Mock would fail 

## methods 
    - ON_CALL:
        - it wont fail if it didnot be called
        - ON_CALL(object_name,method_name(parameter)).WillBeDefault(Return(200))

    - EXPECT_CALL:
        - if fails if it is not called 

    - Times():  
        - number of times to be called 

    - Times(0):
        - means it should not be called at all

    - WillOnce():
        - the first time 

    - WillRepeatedly():
        - everytime after WillOnce

## forcing order 
    - Insequence:
        - we use Sequence to tell the seqence in which calls should be happened 

    - After:
        - assign the return of the expect call in a variable 
        - we call after on it 

    - Insequence:
        - an instante which would enforce sequence in this scope 

## actions
    - DoDefault():
        - this would do what i defined in Oncall

    - Invoke(functionname):
        - call  with the same parameter which is passed to Expect 
        - return value would be what the function is defined 
    
    - InvokeWithoutArgs(f):
        - call wihtout any args