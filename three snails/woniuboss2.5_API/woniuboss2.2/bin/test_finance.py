#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss2.tools.utility import Utility
from woniuboss2.lib.finance import Finance
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')

#新增流水
test_addFinancial_info = Utility.get_excel_to_tuple(data_config_info[13])
#上月查询
test_Query_lastmonth_info = Utility.get_excel_to_tuple(data_config_info[14])
#本月查询
test_Query_thismonth_info = Utility.get_excel_to_tuple(data_config_info[15])
#学员缴费
test_studentpayment_info = Utility.get_excel_to_tuple(data_config_info[16])


class TestFinance(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    # 新增流水
    @parameterized.expand(test_addFinancial_info)
    def test_addFinancial(self, addFinancial_url, post, addFinancial_data, status_code, content):
        finance_addFinancial_resp = Finance().addFinancial(addFinancial_url, addFinancial_data)
        actual = finance_addFinancial_resp.text
        # 断言
        self.assertEqual(actual, content)

    #学员缴费
    @parameterized.expand(test_studentpayment_info)
    def test_payment(self, payment_url, post,payment_data, status_code, content):
        finance_payment_resp = Finance().payment(payment_url, payment_data)
        actual = finance_payment_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(test_Query_lastmonth_info)
    def test_Query_lastmonth(self, Query_lastmonth_url, post, Query_lastmonth_data, status_code, content):
        finance_Query_lastmonth_resp = Finance().Query_lastmonth(Query_lastmonth_url, Query_lastmonth_data)
        actual = finance_Query_lastmonth_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(test_Query_thismonth_info)
    def test_Query_thismonth(self, Query_thismonth_url, post, Query_thismonth_data, status_code, content):
        finance_Query_thismonth_resp = Finance().Query_thismonth(Query_thismonth_url,Query_thismonth_data)
        actual = finance_Query_thismonth_resp.text
        # 断言
        self.assertEqual(actual, content)

if __name__ == '__main__':
    unittest.main(verbosity=2)