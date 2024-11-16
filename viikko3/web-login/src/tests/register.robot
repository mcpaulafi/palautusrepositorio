*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle2
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Register Page
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  ka
    Set Password Confirmation  ka
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  ralle
    Set Password  kalaralle
    Set Password Confirmation  kalaralle
    Submit Credentials
    Register Should Fail With Message  Password should consist of letters a-z and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  pantti
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Register Page
    Set Username  pantti
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Submit Credentials
    Register Should Fail With Message  User with username pantti already exists

*** Keywords ***
Register Should Succeed
    Register Page Should Be Open

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123  kalle123
    Go To Register Page