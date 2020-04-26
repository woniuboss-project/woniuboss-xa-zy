*** Settings ***
Library           RequestsLibrary
Resource          login.txt
Resource          order_refund.txt

*** Test Cases ***
order_refund
    登录
    退货
