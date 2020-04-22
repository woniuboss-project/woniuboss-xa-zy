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














