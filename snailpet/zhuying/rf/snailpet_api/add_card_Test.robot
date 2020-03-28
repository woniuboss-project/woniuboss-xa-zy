*** Settings ***
Library           RequestsLibrary
Resource          login.txt
Resource          add_card.txt

*** Test Cases ***
add card
    登录
    添加会员卡
