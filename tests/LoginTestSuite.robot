*** Settings ***
Library    ../services/UI/LoginService.py
Library    ../services/API/UserService.py

*** Test Cases ***
TC1 New Created User Able To Login
#    When Create User API
    Login    pashka    XjKSG64
    Check Is User First Name Present
#
#TC2 Deleted User Cannot Login
#    When Create User API
#    And Delete User API
#    And Login
#    Then Check Is Login Error Message Present
#
#TC3 User Could Get Propper Error If Enter Incorrect Login Or Password
#    When Create User API
#    And Login With Incorrect Password
#    Then Check Is Login Error Message Present
