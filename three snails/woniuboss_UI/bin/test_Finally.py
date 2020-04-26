#!/usr/bin/env python
# -*- coding:utf-8 -*-
#====#====#====#====
#Author:
#CreatDate:
#Version:
#====#====#====#====
import unittest

from woniuboss_UI.lib.login import Login
from woniuboss_UI.tools.utility import Utility
from  woniuboss_UI.lib.finally_test import Finally_test
from selenium import webdriver
from parameterized import parameterized
#获取excel文件内容
exlce = '../data/WoniuBoss_info.xlsx'
data = Utility.get_excel_to_tuple(exlce,'综合成绩',1,4,3,4)
login_data = Utility.get_excel_to_tuple(exlce,'login',1,2,3,4)

class Test_Finally(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://192.168.1.113:8080/WoniuBoss4.0')
        cls.driver.implicitly_wait(20)
        Login().do_login(cls.driver, login_data)
        Finally_test().open_finally(cls.driver)
    @parameterized.expand(data)
    def test_finally(self,data):
        Finally_test().all_opration(self.driver,data)
        try:
            name = self.driver.find_element_by_xpath("//table[@id='pe-result']/tbody/tr/td[1]").text
        except:
            actual = 'fail'
        else:
            print(name)
            print(data['姓名'])
            if name == data['姓名']:
                actual = 'success'
            else:
                actual = 'fail'
        self.assertEquals(actual, data['expect'])
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

# if __name__ == '__main__':
#     Test_Finally().test_finally()





