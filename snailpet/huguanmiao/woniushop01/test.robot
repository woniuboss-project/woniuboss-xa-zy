*** Settings ***
Resource          login_Process.txt
Resource          vipcard.txt

*** Test Cases ***
login
    登录流程    18700556871    123456    1

add_vipdcard
    新增流程    至尊卡    10000
