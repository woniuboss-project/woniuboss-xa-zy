from selenium.webdriver.common.by import By

from woniuboss4.tools.service import Service
from woniuboss4.tools.utility import Utility
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 查询资源
test_query_resource_info = Utility.get_excel_to_tuple(data_config_info[1])
test_transfer_query_info=Utility.get_excel_to_tuple(data_config_info[2])
test_common_query_info=Utility.get_excel_to_tuple(data_config_info[3])
test_add_resource_info=Utility.get_excel_to_tuple(data_config_info[4])

class TestResource(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver=Service.get_driver('..\\config\\base.conf')
        from woniuboss4.lib.resource import Resource
        cls.resource=Resource(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

     #培训资源
     # 查询资源
    @parameterized.expand(test_query_resource_info)
    def test_query_resource(self, stime, etime, name,expect):
        query_resource_data = {'stime': stime, 'etime': etime,'name': name}
        self.resource.query_resource('..\\config\\base.conf', query_resource_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '#personal-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(15) > button:nth-child(2)') or Service.is_element_present(self.driver, By.CSS_SELECTOR,'.no-records-found > td:nth-child(1)'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, expect)

    #新增资源
    @parameterized.expand(test_add_resource_info)
    def test_query_resource(self, name, phone,expect):
        add_resource_data = {'name': name, 'phone': phone}
        self.resource.add_resource('..\\config\\base.conf', add_resource_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '.bootbox-body'):
            actual = 'add_successful'
        else:
            actual = 'add_failed'
        # 断言
        self.assertEqual(actual, expect)

    #废弃资源
    def test_abandon_resource(self):
        self.resource.abandon_resource('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '#personal-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2) > div:nth-child(1)'):
            actual = 'abandon_successful'
        else:
            actual = 'abandon_failed'
        # 断言
        self.assertEqual(actual, 'abandon_successful')

    #转交资源
    #查询资源
    @parameterized.expand(test_transfer_query_info)
    def test_transfer_query(self, info,expect):
        transfer_query_data = {'info': info}
        self.resource.transfer_query('..\\config\\base.conf', transfer_query_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '#transmit-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2) > div:nth-child(1)') or Service.is_element_present(self.driver, By.CSS_SELECTOR,'.no-records-found > td:nth-child(1)'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, expect)

    #查看简历
    def test_look_resume(self):
        self.resource.look_resume('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '.modal-lg > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    #转交资源
    def test_turn_resource(self):
        self.resource.turn_resource('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '.bootbox-body'):
            actual = 'turn_successful'
        else:
            actual = 'turn_failed'
        # 断言
        self.assertEqual(actual, 'turn_successful')

    #公共资源
    #查询
    @parameterized.expand(test_common_query_info)
    def test_common_query(self, info,expect):
        common_query_data = {'info': info}
        self.resource.common_query('..\\config\\base.conf', common_query_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '#public-pool-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2) > div:nth-child(1)') or Service.is_element_present(self.driver, By.CSS_SELECTOR,'.no-records-found > td:nth-child(1)'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, expect)

    #认领资源
    def test_claim_resource(self):
        self.resource.claim_resource('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '.bootbox-body'):
            actual = 'claim_successful'
        else:
            actual = 'claim_failed'
        # 断言
        self.assertEqual(actual, 'claim_successful')




if __name__ == '__main__':
    unittest.main(verbosity=2)