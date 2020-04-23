# 报表中心ui测试
from woniuboss.tools.service import Service

class Password:
    def __init__(self,driver):
        self.driver = driver

    #解密
    def click_decode_button(self):
        self.driver.find_element_by_id('btn-decrypt').click()

    #输入密码
    def input_password(self,password):
        psword = self.driver.find_element_by_name('secondPass')
        Service.send_input(psword, password)

    #点击确定按钮
    def click_OK_button(self):
        self.driver.find_element_by_css_selector('#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #二级解密动作组织
    def second_password(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_decode_button()
        self.input_password('Woniu123')
        self.click_OK_button()

    #点击修改密码
    def click_change_password(self):
        self.driver.find_element_by_link_text('密码修改').click()

    #点击登录密码
    def click_login_password_button(self):
        self.driver.find_element_by_id('password').click()

    # 输入原登录密码
    def input_oldpw(self, oldpw):
        psword = self.driver.find_element_by_css_selector('#resetInfo > div:nth-child(1) > input:nth-child(1)')
        Service.send_input(psword, oldpw)

    #输入新登录密码
    def input_newpw1(self, newpw1):
        psword = self.driver.find_element_by_css_selector('#resetInfo > div:nth-child(2) > input:nth-child(1)')
        Service.send_input(psword, newpw1)

    #确认新登录密码
    def input_newpw2(self, newpw2):
        psword = self.driver.find_element_by_css_selector('#resetInfo > div:nth-child(3) > input:nth-child(1)')
        Service.send_input(psword, newpw2)

    #点击确认按钮
    def click_sure_button(self):
        self.driver.find_element_by_css_selector('#panel-password > div:nth-child(2) > button:nth-child(1)').click()

    #修改登录密码动作组织
    def change_login_password(self,base_config_path, change_login_password_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password()
        self.click_login_password_button()
        self.input_oldpw(change_login_password_data['oldpw'])
        self.input_newpw1(change_login_password_data['newpw1'])
        self.input_newpw2(change_login_password_data['newpw2'])
        self.click_sure_button()

    #点击二级密码
    def click_second_password(self):
        self.driver.find_element_by_id('password2').click()

    # 输入原登录密码
    def input_second_oldpw(self, oldpw):
        psword = self.driver.find_element_by_css_selector('#pass2Form > div:nth-child(1) > input:nth-child(1)')
        Service.send_input(psword, oldpw)

    # 输入新登录密码
    def input_second_newpw1(self, newpw1):
        psword = self.driver.find_element_by_css_selector('#pass2Form > div:nth-child(2) > input:nth-child(1)')
        Service.send_input(psword, newpw1)

    # 确认新登录密码
    def input_second_newpw2(self, newpw2):
        psword = self.driver.find_element_by_css_selector('#pass2Form > div:nth-child(3) > input:nth-child(1)')
        Service.send_input(psword, newpw2)

    # 点击确认按钮
    def click_second_sure_button(self):
        self.driver.find_element_by_css_selector('#panel-password2 > div:nth-child(2) > button:nth-child(1)').click()

    #修改二级密码动作组织
    def change_second_password(self,base_config_path, change_second_password_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password()
        self.click_second_password()
        self.input_oldpw(change_second_password_data['oldpw'])
        self.input_newpw1(change_second_password_data['newpw1'])
        self.input_newpw2(change_second_password_data['newpw2'])
        self.click_second_sure_button()
