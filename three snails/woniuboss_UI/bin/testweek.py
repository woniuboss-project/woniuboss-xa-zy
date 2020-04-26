import unittest
from time import sleep
from selenium.webdriver.common.by import By
from woniuboss_UI.lib.week_test import Weekgrade
from woniuboss_UI.tools.utility import Utility
from woniuboss_UI.tools.service import Service
from woniuboss_UI.lib.login import Login
from parameterized import parameterized



week_grade_query_info=Utility.read_xls("..\\data\\WoniuBoss_info.xlsx","周考成绩",1,3,3,4)
week_grade_query_params=[]
for week_grade in week_grade_query_info:
    week_grade_tup=(week_grade["area"],week_grade["cname"],week_grade["name"],week_grade["expect"])
    week_grade_query_params.append(week_grade_tup)

week_grade_upload_info=Utility.read_xls("..\\data\\WoniuBoss_info.xlsx", "周考成绩", 3, 4, 3, 4)
week_grade_upload_params=[]
for week_grade_upload in week_grade_upload_info:
    week_grade_tup=(week_grade_upload["cname"],week_grade_upload["stage"],week_grade_upload["weeks"],week_grade_upload["filepath"],week_grade_upload["expect"])
    week_grade_upload_params.append(week_grade_tup)

record_entry_info= Utility.read_xls("..\\data\\WoniuBoss_info.xlsx", "周考成绩", 4, 5, 3, 4)
record_entry_params=[]
for record_entry in record_entry_info:
    record_entry_tup=(record_entry["cname"],record_entry["stage"],record_entry["weeks"],record_entry["grade"],record_entry["expect"])
    record_entry_params.append(record_entry_tup)

edit_test_grade_info=Utility.read_xls("..\\data\\WoniuBoss_info.xlsx", "周考成绩", 5, 6, 3, 4)
edit_test_grade_params=[]
for edit_test_grade in edit_test_grade_info:
    edit_test_grade_tup=(edit_test_grade["grade"],edit_test_grade["expect"])
    edit_test_grade_params.append(edit_test_grade_tup)
exlce = '../data/WoniuBoss_info.xlsx'
login_data = Utility.unitily.get_list_excel(exlce,'login',1,2,3,4)
class Testweek(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #打开应用的首页
        cls.driver=Service.open_page()
        Login().do_login(cls.driver,login_data)
        sleep(2)
        cls.driver.find_element_by_partial_link_text("学员管理").click()
        sleep(2)
        cls.driver.find_element_by_partial_link_text("周考成绩").click()
        sleep(2)
        cls.tw=Weekgrade()

    #周考成绩查询
    @parameterized.expand(week_grade_query_params)
    def test_week_grade_query(self,area,cname,weeks,expect):
        week_query_data=(area,cname,weeks)
        self.tw.week_grade_query(self.driver,week_query_data)
        #判断录入按钮，有则查询成功，没则失败
        if Service.is_element_present(self.driver,By.XPATH,"/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[9]/button"):

            actual="test_week_grade_query_success"
        else:
            actual="test_week_grade_query_fail"
        #断言
        self.assertEqual(actual,expect)
        sleep(3)

    #查看模块
    def test_view_template(self):
        #查看模块
        handle=self.driver.current_window_handle
        self.tw.view_template(self.driver)
        sleep(2)
        #跳到另外一个页面上，如果句柄是两个
        handles=self.driver.window_handles
        if len(handles) ==2:
            actual="test_view_template_success"
        else:
            actual = "test_view_template_fail"
        expect="test_view_template_success"
        #跳到上一个页面
        self.driver.switch_to.window(handle)
        self.assertEqual(actual,expect)



# 周考导入
    @parameterized.expand(week_grade_upload_params)
    def test_week_grade_upload(self,cname,stage,weeks,filepath,expect):
        week_upload_data=(cname,stage,weeks,filepath)
        print(week_upload_data)
        self.tw.week_grade_upload(self.driver,week_upload_data)
        sleep(2)
        if  "上传内容不正确" in self.tw.upload_resp(self.driver):
            actual="test_week_grade_upload_fail"
            self.tw.upload_resp_btn(self.driver)
        else:
            actual="test_week_grade_upload_success"
        self.assertEqual(actual,expect)
        sleep(3)

#数据导出测试
    def test_data_export(self):
        self.tw.btn_data_export(self.driver)
        actual="test_data_export_success"
        expect="test_data_export_success"
        self.assertEqual(actual,expect)

# 周考记录录入
    @parameterized.expand(record_entry_params)
    def test_record_entry(self,cname,stage,weeks,grade,expect):
        test_record_data=(cname,stage,weeks,grade)
        self.tw.record_entry(self.driver,test_record_data)
        actual="test_record_entry_fail"
        self.assertEqual(actual,expect)




#修改周考考分数
    @parameterized.expand(edit_test_grade_params)
    def test_edit_test_grade(self,grade,expect):
        test_edit_test_grade_data=(grade)
        print(test_edit_test_grade_data)
        self.tw.edit_test_grade(self.driver,test_edit_test_grade_data)
        #周考
        grade_resp=self.driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[5]").text
        if grade_resp==grade:
            actual="test_edit_test_grade_success"
        else:
            actual="test_edit_test_grade_fail"
        self.assertEqual(actual,expect)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
