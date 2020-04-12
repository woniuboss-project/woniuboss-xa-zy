#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from woniuboss2.tools.utility import Utility
from woniuboss2.lib.employment import Employment
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
#技术面试
test_Interview_info = Utility.get_excel_to_tuple(data_config_info[19])
#就业管理
test_obtainEmployment_info = Utility.get_excel_to_tuple(data_config_info[20])

class TestEmployment(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    # 技术面试
    @parameterized.expand(test_Interview_info)
    def test_Interview(self, Interview_url,post, Interview_data, status_code,content):
        Employment_Interview_resp = Employment().Interview(Interview_url, Interview_data)
        actual = Employment_Interview_resp.text
        # 断言
        self.assertEqual(actual, content)

    # 就业管理
    @parameterized.expand(test_obtainEmployment_info)
    def test_obtainEmployment(self, obtainEmployment_url, post, obtainEmployment_data, status_code, content):
        Employment_obtainEmployment_resp = Employment().Interview(obtainEmployment_url, obtainEmployment_data)
        actual = Employment_obtainEmployment_resp.text
        # 断言
        self.assertEqual(actual, content)


if __name__ == '__main__':
    unittest.main(verbosity=2)