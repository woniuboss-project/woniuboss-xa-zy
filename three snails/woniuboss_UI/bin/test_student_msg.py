#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import time
from woniuboss_UI.tools.utility import Utility
import unittest
from parameterized import parameterized
from woniuboss_UI.lib.student_msg import Student_msg
from selenium import webdriver

query_data = Utility.get_excel_to_tuple('..\\data\\WoniuBoss_info.xlsx','student',1,3,3,4)
print(query_data)
info = []
for data in query_data:
    tup = (data[0]['name'],data[0]['expect'])
    info.append(tup)
print(info)
amend_data = Utility.get_excel_to_tuple('..\\data\\WoniuBoss_info.xlsx','student',3,6,3,4)
print(amend_data)
info1 = []
for data in amend_data:
    tup = (data[0]['phone'],data[0]['qq'],data[0]['school'],data[0]['expect'])
    info1.append(tup)
# print(info1)
class Test_student_msg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Sm = Student_msg()

    @parameterized.expand(info)
    def test_query_info(self,name,expect):
        self.Sm.query_info((name,))
        time.sleep(2)
        a = self.Sm.driver.find_element_by_xpath(
            "/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td").text
        if a == '无符合条件的记录':
            act = 'query_failed'
        else:
            act = 'query_successful'
        self.assertEqual(act,expect)

    # @parameterized.expand(info1)
    # def test_amend_info(self, phone,qq,school, expect):
    #     self.Sm.amend_info(self.driver, (phone,qq,school))
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath(f'//table[@id="stuInfo_table"]/tbody/tr[2]/td[12]/button[1]').click()
    #     text1 = self.driver.find_element_by_xpath("/html/body/div[11]/div/div/form/div/div[1]/div[1]/div[4]/input").text
    #     if str(text1) == str(phone):
    #         act = 'amend_successful'
    #     else:
    #         act = 'amend_failed'
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath("/html/body/div[12]/div/div/div[1]/button/span[1]").click()
    #     self.assertEqual(act, expect)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)

