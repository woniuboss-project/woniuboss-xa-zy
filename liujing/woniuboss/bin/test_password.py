from selenium.webdriver.common.by import By
from woniuboss.tools.service import Service
from woniuboss.tools.utility import Utility
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 登录密码数据
test_change_login_password_info = Utility.get_excel_to_tuple(data_config_info[6])
# 二级密码数据
test_change_second_password_info = Utility.get_excel_to_tuple(data_config_info[7])

class TestPassword(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = Service.get_driver('..\\config\\base.conf')
        from woniuboss.lib.password import Password
        cls.password = Password(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    # 修改登录密码功能测试
    @parameterized.expand(test_change_login_password_info)
    def test_query_console(self, oldpw, newpw1,newpw2, expect):
        change_login_password_data = {'oldpw': oldpw, 'newpw1': newpw1,'newpw2': newpw2}
        self.password.change_login_password('..\\config\\base.conf', change_login_password_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR, '#panel-password-success > div:nth-child(2) > button:nth-child(1)'):
            actual = 'change_successful'
        else:
            actual = 'change_failed'
        # 断言
        self.assertEqual(actual,expect)

    # 修改二级密码功能测试
    @parameterized.expand(test_change_second_password_info)
    def test_query_console(self, oldpw, newpw1, newpw2, expect):
        change_second_password_data = {'oldpw': oldpw, 'newpw1': newpw1, 'newpw2': newpw2}
        self.password.change_second_password('..\\config\\base.conf', change_second_password_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,
                                      '#panel-password-success > div:nth-child(2) > button:nth-child(1)'):
            actual = 'change_successful'
        else:
            actual = 'change_failed'
        # 断言
        self.assertEqual(actual, expect)


