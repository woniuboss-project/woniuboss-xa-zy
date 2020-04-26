#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from time import sleep
from selenium.webdriver.common.by import By

from woniuboss_UI.lib.month_test import Month_test
from woniuboss_UI.tools.utility import Utility
from woniuboss_UI.tools.service import Service
from parameterized import parameterized
from woniuboss_UI.lib.login import Login

stage_grade_query_info=Utility.get_excel_to_tuple("..\\data\\WoniuBoss_info.xlsx","阶段考评",1,2,3,4)
stage_grade_upload_info=Utility.get_excel_to_tuple("..\\data\\WoniuBoss_info.xlsx", "阶段考评", 2, 3, 3, 4)

    # 获取excel文件内容
exlce = '../data/WoniuBoss_info.xlsx'
data = Utility.get_list_excel(exlce,'login',2,3,3,4)

class Test_month(unittest.TestCase):
    def __init__(self):
        self.driver = driver

    @classmethod
    def setUpClass(cls):
        # 打开首页
        cls.driver = Service.open_page()
        Login().do_login(cls.driver,data)
        sleep(2)
        cls.driver.find_element_by_partial_link_text("学员管理").click()
        sleep(2)
        cls.driver.find_element_by_partial_link_text("阶段考评").click()
        sleep(2)
        cls.tw = Month_test()


    # 阶段考试成绩查询
    @parameterized.expand(stage_grade_query_info)
    def test_stage_grade_query(self,area,cclass,name,expect):
        stage_query_data=(area,cclass,name)

        self.tw.stage_grade_query(self.driver,stage_query_data)
        #判断录入按钮，有则查询成功，没则失败
        if Service.is_element_present(self.driver,By.CSS_SELECTOR,'#pe-result > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(9) > button:nth-child(1)'):

            actual="test_stage_grade_query_success"
        else:
            actual="test_stage_grade_query_fail"
        #断言
        self.assertEqual(expect,actual)



    # 阶段考试导入
    @parameterized.expand(stage_grade_upload_info)
    def test_stage_grade_upload(self, class1, stage1, filepath, expect):
        stage_upload_data = (class1, stage1, filepath)
        print(stage_upload_data)
        self.tw.stage_grade_upload(self.driver,stage_upload_data)
        sleep(2)
        if "上传内容不正确" in self.tw.upload_resp(self.driver):
            actual = "test_stage_grade_upload_fail"
            self.tw.upload_resp_button(self.driver)
        else:
            actual = "test_satge_grade_upload_success"
        self.assertEqual(actual, expect)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
if __name__ == '__main__':
    unittest.main(verbosity=2)

