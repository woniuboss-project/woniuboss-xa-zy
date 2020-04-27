from selenium.webdriver.common.by import By

from woniuboss4.tools.service import Service
from woniuboss4.tools.utility import Utility
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 查询资源
test_query_resource_info = Utility.get_excel_to_tuple(data_config_info[1])


class TestResource(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver=Service.get_driver('..\\config\\base.conf')
        from woniuboss4.lib.resource import Resource
        cls.resource=Resource(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

     # 查询资源
    @parameterized.expand(test_query_resource_info)
    def test_query_resource(self, stime, etime, name,expect):
        query_resource_data = {'stime': stime, 'etime': etime,'name': name}
        self.resource.query_resource('..\\config\\base.conf', query_resource_data)
        if Service.is_element_present(self.driver, By.XPATH,
                                      '/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[1]').text == '姓名':
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)