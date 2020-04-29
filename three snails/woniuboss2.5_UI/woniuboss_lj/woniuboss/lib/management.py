# 后台管理ui测试
from woniuboss.tools.service import Service
import time
class Management:

    def __init__(self,driver):
        self.driver = driver

    # 解密
    def click_decode_button(self):
        self.driver.find_element_by_id('btn-decrypt').click()

    # 输入密码
    def input_password(self, password):
        psword = self.driver.find_element_by_name('secondPass')
        Service.send_input(psword, password)

    # 点击确定按钮
    def click_OK_button(self):
        self.driver.find_element_by_css_selector(
            '#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    # 二级解密动作组织
    def second_password(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_decode_button()
        self.input_password('Woniu123')
        self.click_OK_button()

    #点击后台管理
    def click_management(self):
        self.driver.find_element_by_css_selector('a.list-group-item:nth-child(10)').click()

    # 点击菜单管理
    def click_menu_button(self):
        self.driver.find_element_by_css_selector('ul.nav-tabs:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()

    # 点击资源树
    def click_tree_button(self):
        self.driver.find_element_by_css_selector(
            'button.btn-padding:nth-child(1)').click()

    #点击新增资源
    def click_add_button(self):
        self.driver.find_element_by_xpath(
            '//*[@id="addBtn_res_tree_1"]').click()

    #输入资源名
    def input_name(self, res_name):
        name = self.driver.find_element_by_css_selector('#addRes-form > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
        Service.send_input(name, res_name)

    # 输入资源名
    def input_url(self, res_url):
        url = self.driver.find_element_by_css_selector(
            '#addRes-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(2)')
        Service.send_input(url, res_url)

    # 输入描述
    def input_des(self, res_des):
        des = self.driver.find_element_by_css_selector(
            '#addRes-form > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > textarea:nth-child(2)')
        Service.send_input(des, res_des)

    #点击关闭按钮
    def click_close_button(self):
        self.driver.find_element_by_css_selector(
            '#addRes-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)').click()

    # 新增资源动作组织
    def add_resource(self, base_config_path, add_resource_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        time.sleep(5)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_menu_button()
        self.click_tree_button()
        self.click_add_button()
        self.input_name(add_resource_data['res_name'])
        self.input_url(add_resource_data['res_url'])
        self.input_des(add_resource_data['res_des'])
        # self.click_close_button()

    #点击编辑资源
    def click_edit_button(self):
        self.driver.find_element_by_id(
            'res_tree_1_edit').click()

    #输入资源名
    def input_res_name(self, res_name):
        name = self.driver.find_element_by_id('res_tree_1_span')
        Service.send_input(name, res_name)

    #编辑资源动作组织
    def edit_res(self,base_config_path, edit_resource_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_menu_button()
        self.click_edit_button()
        self.input_res_name(edit_resource_data['res_name'])
        # self.click_close_button()

    #点击删除资源
    def click_remove_button(self):
        self.driver.find_element_by_id(
            'res_tree_1_remove').click()

    #点击确认删除按钮
    def click_remove_ok_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()

    #删除资源动作的组织
    def remove_res(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_menu_button()
        self.click_remove_button()
        self.click_remove_ok_button()
        self.click_close_button()

    #点击设置按钮
    def click_set_button(self):
        self.driver.find_element_by_css_selector('#res-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(1)').click()

    #输入角色名
    def input_role_name(self, role_name):
        name = self.driver.find_element_by_name('role.name')
        Service.send_input(name, role_name)

    # 输入描述
    def input_role_des(self, role_des):
        des = self.driver.find_element_by_name('role.des')
        Service.send_input(des, role_des)

    #点击保存
    def click_saveSet(self):
        self.driver.find_element_by_id('saveSetRole').click()

    #点击关闭按钮
    def click_save_close(self):
        self.driver.find_element_by_css_selector('#setRole-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)').click()

    #设置动作的组织
    def set(self,base_config_path,set_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_menu_button()
        self.click_set_button()
        self.input_role_name(set_data['role_name'])
        self.input_role_des(set_data['role_des'])
        self.click_saveSet()
        self.click_save_close()

    #点击角色管理
    def click_role(self):
        self.driver.find_element_by_css_selector('ul.nav-tabs:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()

    #点击新增
    def click_add_role_button(self):
        self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()

    #输入角色名
    def input_add_role_name(self, add_role_name):
        name = self.driver.find_element_by_name('role.name')
        Service.send_input(name, add_role_name)

    # 输入描述
    def input_add_role_res(self, add_role_des):
        name = self.driver.find_element_by_name('role.des')
        Service.send_input(name, add_role_des)

    #点击保存
    def click_add_role_save(self):
        self.driver.find_element_by_id('saveAddRole').click()

    #点击确认
    def click_add_role_ok(self):
        self.driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #新增角色动作组织
    def add_role(self,base_config_path,add_role_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_role()
        self.click_add_role_button()
        self.input_add_role_name(add_role_data['add_role_name'])
        self.input_add_role_res(add_role_data['add_role_des'])
        self.click_add_role_save()
        self.click_add_role_ok()


    #点击修改按钮
    def click_role_edit_button(self):
        self.driver.find_element_by_css_selector('#role-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(2)').click()

    #输入修改角色名
    def input_edit_role_name(self,edit_role_name):
        name = self.driver.find_element_by_name('role.name')
        Service.send_input(name, edit_role_name)

    # 输入修改描述
    def input_edit_role_des(self, edit_role_des):
        des = self.driver.find_element_by_name('role.des')
        Service.send_input(des, edit_role_des)

    #点击修改角色保存按钮
    def click_edit_role_save(self):
        self.driver.find_element_by_id('saveEidtRole').click()

    #点击关闭
    def click_edit_role_close(self):
        self.driver.find_element_by_css_selector('#editRole-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)').click()

    #修改角色动作组织
    def edit_role(self,base_config_path,edit_role_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_role()
        self.click_role_edit_button()
        self.input_edit_role_name(edit_role_data['edit_role_name'])
        self.input_edit_role_des(edit_role_data['edit_role_des'])
        self.click_edit_role_save()
        self.click_edit_role_close()

    #点击用户管理
    def click_user(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/li[3]/a').click()

    #输入用户名
    def input_username(self,username):
        name = self.driver.find_element_by_name('userName')
        Service.send_input(name, username)

    #点击查询
    def click_user_query(self):
        self.driver.find_element_by_css_selector('div.con-margin:nth-child(2) > button:nth-child(4)').click()

    #查询用户动作组织
    def query_username(self,base_config_path,query_username_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_user()
        self.input_username(query_username_data['username'])
        self.click_user_query()

    #点击用户管理设置
    def click_user_set(self):
        self.driver.find_element_by_css_selector('#user-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > button:nth-child(1)').click()

    #输入用户管理角色名
    def input_username_role(self,username_role):
        name = self.driver.find_element_by_name('user.name')
        Service.send_input(name, username_role)

    #输入用户管理描述
    def input_username_des(self,username_des):
        name = self.driver.find_element_by_name('user.des')
        Service.send_input(name, username_des)

    #点击保存按钮
    def click_user_save_button(self):
        self.driver.find_element_by_id('saveSetUser').click()

    #点击关闭按钮
    def click_user_close_button(self):
        self.driver.find_element_by_css_selector('#setUser-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)').click()

    #用户管理设置动作组织
    def user_set(self,base_config_path,user_set_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_user()
        self.click_user_set()
        self.input_username_role(user_set_data['username_role'])
        self.input_username_des(user_set_data['username_des'])
        self.click_user_save_button()
        self.click_user_close_button()

    #点击字典管理
    def click_dictionary(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/li[4]/a').click()

    #点击新增
    def click_dictionary_add_button(self):
        self.driver.find_element_by_css_selector('#dict-type-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(1)').click()

    #输入字典标签
    def input_dict_value(self,dict_value):
        value = self.driver.find_element_by_name('dd.dict_value')
        Service.send_input(value, dict_value)

    #输入字典键值
    def input_dict_key(self,dict_key):
        key = self.driver.find_element_by_name('dd.dict_key')
        Service.send_input(key, dict_key)

    #输入序号
    def input_dict_sort(self,dict_sort):
        sort = self.driver.find_element_by_name('dd.sort')
        Service.send_input(sort, dict_sort)

    #输入备注
    def input_dict_remarks(self,dict_remarks):
        remarks = self.driver.find_element_by_name('dd.remarks')
        Service.send_input(remarks, dict_remarks)

    #点击保存
    def click_dict_save_button(self):
        self.driver.find_element_by_css_selector('#addOption-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #点击关闭
    def click_dict_close_button(self):
        self.driver.find_element_by_css_selector('#addOption-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)').click()

    #字典管理新增动作组织
    def dict_add(self,base_config_path,dict_add_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_dictionary()
        self.click_dictionary_add_button()
        self.input_dict_value(dict_add_data['dict_value'])
        self.input_dict_key(dict_add_data['dict_key'])
        self.input_dict_sort(dict_add_data['dict_sort'])
        self.input_dict_remarks(dict_add_data['dict_remarks'])
        self.click_dict_save_button()
        self.click_dict_close_button()

    #点击启用
    def click_start_button(self):
        self.driver.find_element_by_css_selector('#dict-type-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(2)').click()

    #点击确认按钮
    def click_start_ok_button(self):
        self.driver.find_element_by_css_selector('button.btn-primary:nth-child(2)').click()

    #启用动作组织
    def start(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_dictionary()
        self.click_start_button()
        self.click_start_ok_button()

    #点击详情
    def click_details(self):
        self.driver.find_element_by_css_selector('#dict-type-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5) > button:nth-child(3)').click()

    #点击编辑
    def click_details_edit(self):
        self.driver.find_element_by_css_selector('#dict-detail-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > button:nth-child(1)').click()

    #输入字典名称
    def input_dict_typename(self,dict_typename):
        typename = self.driver.find_element_by_name('dict_typename')
        Service.send_input(typename, dict_typename)

    #输入字典名称
    def input_dict_value1(self,dict_value):
        value1 = self.driver.find_element_by_name('dd.dict_value')
        Service.send_input(value1, dict_value)

    # 输入序号
    def input_dict_sort1(self, dict_sort):
        sort1 = self.driver.find_element_by_name('dd.sort')
        Service.send_input(sort1, dict_sort)

    # 输入备注
    def input_dict_remarks1(self, dict_remarks):
        remarks1 = self.driver.find_element_by_name('dd.remarks')
        Service.send_input(remarks1, dict_remarks)

    #点击保存
    def click_details_edit_save_button(self):
        self.driver.find_element_by_css_selector('#edit-detail-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #详情编辑动作组织
    def details_edit(self,base_config_path,details_edit_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.click_management()
        self.click_dictionary()
        self.click_details()
        self.click_details_edit()
        self.input_dict_typename(details_edit_data['dict_typename'])
        self.input_dict_value1(details_edit_data['dict_value'])
        self.input_dict_sort1(details_edit_data['dict_sort'])
        self.input_dict_remarks1(details_edit_data['dict_remarks'])
        self.click_details_edit_save_button()










