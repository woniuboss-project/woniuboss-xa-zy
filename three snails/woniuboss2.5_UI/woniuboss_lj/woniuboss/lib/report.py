# 报表中心ui测试
from woniuboss.tools.service import Service
import time
class Report:

    def __init__(self,driver):
        self.driver = driver

    #点击报表中心
    def click_report(self):
        self.driver.find_element_by_css_selector('a.list-group-item:nth-child(1)').click()
        time.sleep(3)

    #点击咨询部
    def click_consult(self):
        self.driver.find_element_by_css_selector('ul.nav-tabs:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
    #选择起始时间
    def input_stime(self,stime):
        Service.remove_readonly(self.driver, 's_consulttime')
        stime_ele = self.driver.find_element_by_name('s_consulttime')
        Service.send_input(stime_ele, stime)

    #选择终止时间
    def input_etime(self,etime):
        Service.remove_readonly(self.driver, 'e_consulttime')
        etime_ele = self.driver.find_element_by_name('e_consulttime')
        Service.send_input(etime_ele, etime)

    #点击搜索按钮
    def click_query_button(self):
        self.driver.find_element_by_link_text('搜索').click()

    # 咨询部查询
    def query_console(self, base_config_path, query_console_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.input_stime(query_console_data['stime'])
        self.input_etime(query_console_data['etime'])
        self.click_query_button()
        time.sleep(5)


    #查询当期
    def click_phase(self):
        self.driver.find_element_by_css_selector('#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(4)').click()

    #查询当期动作组织
    def query_phase(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_phase()
        time.sleep(5)

    # 查询今日
    def click_today(self):
        self.driver.find_element_by_css_selector('#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(5)').click()

    # 查询今日动作组织
    def query_today(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_today()
        time.sleep(5)

    #查询本周
    def click_week(self):
        self.driver.find_element_by_css_selector('#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(6)').click()

    # 查询本周动作组织
    def query_week(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_week()
        time.sleep(5)

    # 查询本月
    def click_month(self):
        self.driver.find_element_by_css_selector(
            '#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(7)').click()

    # 查询本月动作组织
    def query_month(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_month()
        time.sleep(5)

    # 查询上周
    def click_lastweek(self):
        self.driver.find_element_by_css_selector(
            '#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(8)').click()

    # 查询上周动作组织
    def query_lastweek(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_lastweek()
        time.sleep(5)

    # 查询上月
    def click_lastmonth(self):
        self.driver.find_element_by_css_selector(
            '#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(9)').click()

    # 查询上月动作组织
    def query_lastmonth(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_lastmonth()
        time.sleep(5)

    # 查询本年
    def click_year(self):
        self.driver.find_element_by_css_selector(
            '#consulting-1 > div:nth-child(1) > div:nth-child(1) > button:nth-child(10)').click()

    # 查询本年动作组织
    def query_year(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_report()
        self.click_consult()
        self.click_year()
        time.sleep(5)
