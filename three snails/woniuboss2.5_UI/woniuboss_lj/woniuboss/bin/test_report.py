from selenium.webdriver.common.by import By
from woniuboss.tools.service import Service
from woniuboss.tools.utility import Utility
import unittest
from parameterized import parameterized
# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 咨询部数据
test_query_console_info = Utility.get_excel_to_tuple(data_config_info[5])

class TestReport(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = Service.get_driver('..\\config\\base.conf')
        from woniuboss.lib.report import Report
        cls.report = Report(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    # 咨询部报表中心功能测试
    @parameterized.expand(test_query_console_info)
    def test_query_console(self,stime,etime,expect):
        query_console_data = {'stime': stime, 'etime': etime}
        self.report.query_console('..\\config\\base.conf', query_console_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, expect)

    def test_query_phase(self):
        self.report.query_phase('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    def test_query_today(self):
        self.report.query_today('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    def test_query_week(self):
        self.report.query_week('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    def test_query_month(self):
        self.report.query_month('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    def test_query_lastweek(self):
        self.report.query_lastweek('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    def test_query_lastmonth(self):
        self.report.query_lastmonth('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    def test_query_year(self):
        self.report.query_year('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '咨询师'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

if __name__ == '__main__':
    unittest.main(verbosity=2)
