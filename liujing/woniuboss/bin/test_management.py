from selenium.webdriver.common.by import By

from woniuboss.tools.service import Service
from woniuboss.tools.utility import Utility
import unittest
from parameterized import parameterized
# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 咨询部数据
test_add_resource_info = Utility.get_excel_to_tuple(data_config_info[8])

test_edit_resource_info=Utility.get_excel_to_tuple(data_config_info[9])
test_set_info=Utility.get_excel_to_tuple(data_config_info[10])
test_add_role_info=Utility.get_excel_to_tuple(data_config_info[11])
test_edit_role_info=Utility.get_excel_to_tuple(data_config_info[12])
test_query_username_info=Utility.get_excel_to_tuple(data_config_info[13])
test_user_set_info=Utility.get_excel_to_tuple(data_config_info[14])
test_dict_add_info=Utility.get_excel_to_tuple(data_config_info[15])
test_details_edit_info=Utility.get_excel_to_tuple(data_config_info[16])
class TestManagement(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = Service.get_driver('..\\config\\base.conf')
        from woniuboss.lib.management import Management
        cls.management = Management(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    # 菜单管理资源树新增功能测试
    @parameterized.expand(test_add_resource_info)
    def test_add_resource(self,res_name,res_url,res_des,expect):
        add_resource_data = {'res_name': res_name, 'res_url': res_url,'res_des': res_des}
        self.management.add_resource('..\\config\\base.conf', add_resource_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, res_name):
            actual = 'add_successful'
        else:
            actual = 'add_failed'
        # 断言
        self.assertEqual(actual, expect)

    # 菜单管理资源树编辑功能测试
    @parameterized.expand(test_edit_resource_info)
    def test_edit_resource(self, res_name,expect):
        edit_resource_data = {'res_name': res_name}
        self.management.edit_res('..\\config\\base.conf', edit_resource_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, res_name):
            actual = 'edit_successful'
        else:
            actual = 'edit_failed'
        # 断言
        self.assertEqual(actual, expect)

    # 菜单管理资源树删除功能测试
    def test_remove_res(self):
        self.management.remove_res('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.ID, 'res_tree_25_span'):
            actual = 'remove_successful'
        else:
            actual = 'remove_failed'
        # 断言
        self.assertEqual(actual, 'remove_successful')

    #菜单管理设置功能测试
    @parameterized.expand(test_set_info)
    def test_set(self, role_name,role_des ,expect):
        set_data = {'role_name': role_name,'role_des': role_des}
        self.management.set('..\\config\\base.conf', set_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, role_name):
            actual = 'set_successful'
        else:
            actual = 'set_failed'
        # 断言
        self.assertEqual(actual, expect)

    #角色管理新增角色功能测试
    @parameterized.expand(test_add_role_info)
    def test_add_role(self, add_role_name, add_role_des, expect):
        add_role_data = {'add_role_name': add_role_name, 'add_role_des': add_role_des}
        self.management.add_role('..\\config\\base.conf', add_role_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, add_role_name):
            actual = 'add_successful'
        else:
            actual = 'add_failed'
        # 断言
        self.assertEqual(actual, expect)

    #修改角色功能测试
    @parameterized.expand(test_edit_role_info)
    def test_edit_role(self, edit_role_name, edit_role_des, expect):
        edit_role_data = {'edit_role_name': edit_role_name, 'edit_role_des': edit_role_des}
        self.management.edit_role('..\\config\\base.conf', edit_role_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, edit_role_name):
            actual = 'edit_successful'
        else:
            actual = 'edit_failed'
        # 断言
        self.assertEqual(actual, expect)

    #用户管理查询功能测试
    @parameterized.expand(test_query_username_info)
    def test_query_username(self, username, expect):
        query_username_data = {'username': username}
        self.management.query_username('..\\config\\base.conf', query_username_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR, '#user-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > button:nth-child(1)'):
            actual = 'query_successful'
        else:
            actual = 'query_failed'
        # 断言
        self.assertEqual(actual, expect)

    #用户管理设置功能测试
    @parameterized.expand(test_user_set_info)
    def test_user_set(self, username_role,username_des ,expect):
        user_set_data = {'username_role': username_role,'username_des': username_des}
        self.management.user_set('..\\config\\base.conf', user_set_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT,username_role):
            actual = 'set_successful'
        else:
            actual = 'set_failed'
        # 断言
        self.assertEqual(actual, expect)

    #字典管理新增功能测试
    @parameterized.expand(test_dict_add_info)
    def test_dict_add(self, dict_value,dict_key, dict_sort,dict_remarks,expect):
        dict_add_data = {'dict_value': dict_value,'dict_key': dict_key,'dict_sort': dict_sort,'dict_remarks': dict_remarks}
        self.management.dict_add('..\\config\\base.conf', dict_add_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT,dict_value):
            actual = 'add_successful'
        else:
            actual = 'add_failed'
        # 断言
        self.assertEqual(actual, expect)

    #字典管理启用功能测试
    def test_start(self):
        self.management.start('..\\config\\base.conf')
        if Service.is_element_present(self.driver, By.LINK_TEXT, '停用'):
            actual = 'start_successful'
        else:
            actual = 'start_failed'
        # 断言
        self.assertEqual(actual, 'start_successful')

    # 字典管理详情编辑功能测试
    @parameterized.expand(test_details_edit_info)
    def test_details_edit(self, dict_typename, dict_value, dict_sort, dict_remarks, expect):
        details_edit_data = {'dict_typename': dict_typename, 'dict_value': dict_value, 'dict_sort': dict_sort,
                         'dict_remarks': dict_remarks}
        self.management.details_edit('..\\config\\base.conf', details_edit_data)
        if Service.is_element_present(self.driver, By.LINK_TEXT, '正常'):
            actual = 'edit_successful'
        else:
            actual = 'edit_failed'
        # 断言
        self.assertEqual(actual, expect)
