*** Settings ***
Library           RequestsLibrary
Resource          login.txt
Resource          add_customer.txt

*** Test Cases ***
add customer
    登录
    新增会员
