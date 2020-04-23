from woniuboss.tools.service import Service
import time

class FinancialManage:
    def __init__(self,driver):
        self.driver = driver

    def click_add_flow_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(10)').click()

    def input_money(self,moneyNo):
        money = self.driver.find_element_by_id('moneyNo')
        Service.send_input(money,moneyNo)

    def input_countparty(self,counterpartyName):
        countparty = self.driver.find_element_by_id('counterpartyName')
        Service.send_input(countparty,counterpartyName)

    def input_record(self,textarea):
        record = self.driver.find_element_by_id('textarea')
        Service.send_input(record,textarea)

    def click_save_flow(self):
        self.driver.find_element_by_id('changeButton').click()

    #新增流水动作组合
    def add_flow(self,base_config_path, add_flow_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        driver.find_element_by_id('abc').click()
        time.sleep(6)
        self.click_add_flow_button()
        self.input_money(add_flow_data['moneyNo'])
        self.input_countparty(add_flow_data['counterpartyName'])
        self.input_record(add_flow_data['textarea'])
        self.click_save_flow()

    #点击解密按钮
    def click_decode_button(self):
        self.driver.find_element_by_id('btn-decrypt').click()

    # 输入密码
    def input_password(self, password):
        psword = self.driver.find_element_by_name('secondPass')
        Service.send_input(psword, password)

    #点击解密确定按钮
    def click_confirm(self):
        self.driver.find_element_by_css_selector('#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #执行解密动作组合
    def decrypt(self,base_config_path,add_password_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        driver.find_element_by_id('abc').click()
        time.sleep(6)
        self.click_decode_button()
        self.input_password(add_password_data['password'])
        self.click_confirm()

    #点击学员缴费按钮
    def click_student_pay(self):
        self.driver.find_element_by_css_selector('li.active:nth-child(3) > a:nth-child(1)').click()

    #点击缴费/退费按键
    def click_pay_button(self):
        self.driver.find_element_by_css_selector('#nopayStudent-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > button:nth-child(1)').click()

    #随机选择班级
    def choose_class(self):
        s_class = self.driver.find_element_by_id('student_class')
        Service.select_random(s_class)

    #选择缴费状态
    def choose_status(self,stu_status):
        Service.remove_readonly(self.driver, 'stuStatus')
        status = self.driver.find_element_by_id('stuStatus')
        Service.send_input(status,stu_status)


    #输入支付金额
    def input_pay_money(self,money):
        p_money = self.driver.find_element_by_id('stupay')
        Service.send_input(p_money,money)



    #上月查询
    def query_lastmonth(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.driver.find_element_by_id('selectLastMonthAll').click()

    #本月查询
    def query_thismonth(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.driver.find_element_by_id('selectThisMonthAll').click()














