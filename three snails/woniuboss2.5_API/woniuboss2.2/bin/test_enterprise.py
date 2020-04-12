#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import json
import unittest
from parameterized import parameterized

from woniuboss2.lib.enterprise import EtprsManage
from woniuboss2.tools.utility import Utility

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
#新增企业
test_add_company_info= Utility.get_excel_to_tuple(data_config_info[17])
#查询企业
test_query_etprs_info = Utility.get_excel_to_tuple(data_config_info[18])

class TestEnterprise(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    # 新增企业
    @parameterized.expand(test_add_company_info)
    def test_add_company(self, add_company_url, post, add_company_data, status_code, content):
        EtprsManage_add_company_resp = EtprsManage().add_company(add_company_url, add_company_data)
        actual = EtprsManage_add_company_resp.text
        # 断言
        self.assertEqual(actual, content)

    #企业查询
    @parameterized.expand(test_query_etprs_info)
    def test_query_etprs(self, query_etprs_url, post, query_etprs_data, status_code, content):
        EtprsManage_query_etprs_resp = EtprsManage().query_etprs(query_etprs_url, query_etprs_data)
        actual = EtprsManage_query_etprs_resp.text
        # 断言
        self.assertEqual(actual, content)


if __name__ == '__main__':
    unittest.main(verbosity=2)


