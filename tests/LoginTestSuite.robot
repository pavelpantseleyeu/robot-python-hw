*** Settings ***
Library    ../services/UI/LoginService.py
Library    ../services/API/UserService.py

*** Test Cases ***
TC1 New Created User Able To Login
    Create User API
    Login
    Check Is User First Name Present

TC2 Deleted User Cannot Login
    Create User API
    Delete User API
    Login
    Check Is Login Error Message Present

TC3 User Could Get Propper Error If Enter Incorrect Login Or Password
    Create User API
    Login With Incorrect Password
    Check Is Login Error Message Present
