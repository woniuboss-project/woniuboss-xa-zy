import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By

from woniuboss_4.lib.student_info import Student_info
from woniuboss_4.tools.service import Service
from woniuboss_4.tools.utility import Utility

test_config_info = Utility.get_json('..\\config\\testdata.conf')
search_student_info = Utility.get_excel_to_tuple(test_config_info[0])
edit_student_info = Utility.get_excel_to_tuple(test_config_info[1])

class StudentTest(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        self.student = Student_info(self.driver)

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(search_student_info)
    def test_student_search(self,s_direction,s_classname,s_status,s_name,expect):
        search_data = {'direction': s_direction,'classname': s_classname,'status': s_status,'name': s_name}
        self.student.search_action('..\\config\\base.conf', search_data)
        time.sleep(4)
        if s_status == '全部':
            stu_status = '%'
        elif s_status == '未开班':
            stu_status = '01'
        elif s_status == '在校学习':
            stu_status = '02'
        elif s_status == '转就业':
            stu_status = '03'
        elif s_status == '已就业':
            stu_status = '04'
        elif s_status == '已休学':
            stu_status = '05'
        elif s_status == '已失联':
            stu_status = '06'
        else:
            stu_status = '07'

        if s_name == '':
            stu_name = '%'
        else:
            stu_name = s_name

        if s_classname == '全部':
            stu_classname = '%'
        else:
            stu_classname = s_classname

        if s_direction == '全部':
            stu_direction = '%'
        else:
            stu_direction = s_direction

        sql = f"select count(*) from student where student_class_id in (select class_id from class where class_no like '{stu_classname}' " \
              f"and orientation like '{stu_direction}') and status like '{stu_status}' and student_name like '{stu_name}%'"
        result = Utility.query_one(search_student_info, sql)
        sum_text = self.driver.find_element_by_css_selector('#stuInfo > div.bootstrap-table > div.fixed-table-container'
                                                           '> div.fixed-table-pagination > div.pull-left.'
                                                           'pagination-detail > span.pagination-info').text
        if '总共' in sum_text:
            sum_num = sum_text.split('总共 ')[1].split(' 条')[0]
        else:
            sum_num = 0
        if result[0] == int(sum_num):
            actual = 'test query success'
        else:
            actual = 'test query fail'
        self.assertEqual(expect,actual)

    @parameterized.expand(edit_student_info)
    def test_student_edit(self,status,money,QQ,name,number,expect):
        student_data={'newstatus':status,'tuition':money,'qq':QQ,'ContactName':name,'phonenumber':number}
        self.student.edit_stuinfo('..\\config\\base.conf',student_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      'body > div.bootbox.modal.fade.mydialog.in > div > div'):
            text = self.driver.find_element_by_css_selector('body > div.bootbox.modal.fade.mydialog.in > div > '
                                                           'div > div.modal-body > div').text
            if '操作成功' in text:
                actual = 'test-edit-success'
            else:
                actual = 'test-edit-fail'
        else:
            actual = 'test-edit-fail'
        self.assertEqual(actual, expect)

