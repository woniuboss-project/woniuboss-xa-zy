*** Settings ***
Resource          customer_flow.txt

*** Test Cases ***
add customer
    新增会员流程    王明    13401222111    保存成功！
    新增会员流程    朱明    134012    请输入正确的电话号码！

query customer
    查询会员流程    13401222222

edit customer
    修改会员流程    尊贵VIP    保存成功！
