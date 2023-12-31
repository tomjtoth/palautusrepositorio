*** Settings ***
Resource            resource.robot
Resource            login.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Open The Register View


*** Test Cases ***
Register With Valid Username And Password
    Set Username    kalle
    Set Password Twice    kalle123
    Submit Credentials
    Title Should Be    Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username    ka
    Set Password Twice    kalle456
    Submit Credentials
    Register Should Fail With Message    Username complexity requirements unsatisfied

Register With Valid Username And Invalid Password
    Set Username    kalle
    Set Password Twice    kalle
    Submit Credentials
    Register Should Fail With Message    Password complexity requirements unsatisfied

Register With Nonmatching Password And Password Confirmation
    Set Username    kalle
    Set Password    kalle123
    Input Password    password_confirmation    kalle1234
    Submit Credentials
    Register Should Fail With Message    Passwords don't match

Login After Successful Registration
    Set Username    qwer
    Set Password Twice    qwer1234
    Submit Credentials
    Title Should Be    Welcome to Ohtu Application!
    Go To Login Page
    Set Username    qwer
    Set Password    qwer1234
    Click Button    Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username    qqq
    Set Password Twice    qqqqqqqq
    Submit Credentials
    Register Should Fail With Message    Password complexity requirements unsatisfied
    Go To Login Page
    Set Username    qqq
    Set Password    qqqqqqqq
    Click Button    Login
    Login Should Fail With Message    Invalid username or password


*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Submit Credentials
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Twice
    [Arguments]    ${password}
    Input Password    password    ${password}
    Input Password    password_confirmation    ${password}

Open The Register View
    Go To Register Page
    Register Page Should Be Open
