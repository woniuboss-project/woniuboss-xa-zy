*** Settings ***
Resource          card_flow.txt

*** Test Cases ***
add card
    新增会员卡流程    金卡    100    金卡
    新增会员卡流程    银卡    1    银卡
