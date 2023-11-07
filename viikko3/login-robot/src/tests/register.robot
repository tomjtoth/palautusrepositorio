*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  qqq  qwer1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  qqq  qwer1234
    Input New Command
    Input Credentials  qqq  qwer1234
    Output Should Contain  User with username qqq already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  qq  qwer1234
    Output Should Contain  Username complexity requirements unsatisfied

Register With Enough Long But Invald Username And Valid Password
    Input New Command
    Input Credentials  qqq123  qwer1234
    Output Should Contain  Username complexity requirements unsatisfied


Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  qqq  qwer123
    Output Should Contain  Password complexity requirements unsatisfied


Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  qqq  qqqqqqqq
    Output Should Contain  Password complexity requirements unsatisfied
