import time

from woniuboss.tools.service import Service
from selenium import webdriver

class Market:

    def __init__(self,driver):
        self.driver=driver

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

    #点击市场营销
    def market(self):
        self.driver.find_element_by_css_selector('a.list-group-item:nth-child(2)').click()

    # 选择区域
    def select_region(self):
        region_select=self.driver.find_element_by_name('regionSelect')
        Service.select_random(region_select)
    #选择状态
    def select_status(self):
        status_select=self.driver.find_element_by_name('cus.last_status')
        Service.select_random(status_select)
    #选择起始时间
    def input_stime(self,stime):
        Service.remove_readonly(self.driver,'s_time')
        stime_ele = self.driver.find_element_by_name('s_time')
        Service.send_input(stime_ele,stime)
    #选择终止时间
    def input_etime(self,etime):
        Service.remove_readonly(self.driver, 'e_time')
        etime_ele = self.driver.find_element_by_name('e_time')
        Service.send_input(etime_ele, etime)
    #点击查询按钮
    def click_query_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(5)').click()

    #查询资源动作的组合
    def qureyNetCus(self,base_config_path, qureyNetCus_data):
        driver=self.driver
        Service.miss_login(driver,base_config_path)
        self.second_password('..\\config\\base.conf')
        self.market()
        self.select_region()
        self.select_status()
        self.input_stime(qureyNetCus_data['stime'])
        self.input_etime(qureyNetCus_data['etime'])
        self.click_query_button()
        time.sleep(3)

    def query_all(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.market()
        self.click_query_button()
        time.sleep(3)

    #点击新增网络按钮
    def click_add_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(6)').click()

    #随机选择区域
    def select_cus_region(self):
        region_select = self.driver.find_element_by_name('cus.region')
        Service.select_random(region_select)

    #随机选择部门
    def select_department(self):
        department_select=self.driver.find_element_by_name('cus.department_id')
        Service.select_random(department_select)

    #输入电话
    def input_phone(self,cus_phone):
        phone=self.driver.find_element_by_name('cus.tel')
        Service.send_input(phone,cus_phone)

    #输入姓名
    def input_name(self,cus_name):
        name=self.driver.find_element_by_name('cus.name')
        Service.send_input(name,cus_name)

    #随机选择性别
    def select_sex(self):
        sex_select = self.driver.find_element_by_name('cus.sex')
        Service.select_random(sex_select)

    #随机选择最新状态
    def select_last_status(self):
        status_select = self.driver.find_element_by_name('cus.last_status')
        Service.select_random(status_select)

    #输入邮箱
    def input_email(self,cus_email):
        email=self.driver.find_element_by_name('cus.email')
        Service.send_input(email,cus_email)

    #输入QQ
    def input_qq(self,cus_qq):
        qq=self.driver.find_element_by_name('cus.qq')
        Service.send_input(qq,cus_qq)

    #输入学校
    def input_school(self,cus_school):
        school=self.driver.find_element_by_name('cus.school')
        Service.send_input(school,cus_school)

    #随机选择学历
    def select_education(self):
        education_select = self.driver.find_element_by_name('cus.education')
        Service.select_random(education_select)

    #输入专业
    def input_major(self,cus_major):
        major=self.driver.find_element_by_name('cus.major')
        Service.send_input(major,cus_major)

    #输入求职意向
    def input_intent(self,cus_intent):
        intent=self.driver.find_element_by_name('cus.intent')
        Service.send_input(intent,cus_intent)

    #随机选择工作年限
    def select_workage(self):
        workage_select = self.driver.find_element_by_name('cus.workage')
        Service.select_random(workage_select)

    #输入期望薪水
    def input_salary(self,cus_salary):
        salary=self.driver.find_element_by_name('cus.salary')
        Service.send_input(salary,cus_salary)

    #随机选择渠道来源
    def select_source(self):
        source_select = self.driver.find_element_by_name('cus.source')
        Service.select_random(source_select)

    #输入应聘职位
    def input_applposition(self,cus_applposition):
        applposition=self.driver.find_element_by_name('cus.applposition')
        Service.send_input(applposition,cus_applposition)

    #输入年龄
    def input_age(self,cus_age):
        age=self.driver.find_element_by_name('cus.age')
        Service.send_input(age,cus_age)

    #输入教育经历
    def input_eduexp(self,cus_eduexp):
        eduexp=self.driver.find_element_by_name('cus.eduexp')
        Service.send_input(eduexp,cus_eduexp)

    #输入工作经历
    def input_experience(self, cus_experience):
        experience = self.driver.find_element_by_name('cus.experience')
        Service.send_input(experience, cus_experience)

    #输入最后跟踪
    def input_last_tracking(self, cus_last_tracking):
        last_tracking = self.driver.find_element_by_name('cus.last_tracking_remark')
        Service.send_input(last_tracking, cus_last_tracking)

    #点击保存按钮
    def click_save_button(self):
        self.driver.find_element_by_id('addCusBtn').click()

    # 新增网络动作的组合
    def addCus(self, base_config_path, addResModel_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.market()
        self.click_add_button()
        self.select_cus_region()
        self.select_department()
        self.input_phone(addResModel_data['cus_phone'])
        self.input_name(addResModel_data['cus_name'])
        self.select_sex()
        self.select_last_status()
        self.input_email(addResModel_data['cus_email'])
        self.input_qq(addResModel_data['cus_qq'])
        self.input_school(addResModel_data['cus_school'])
        self.select_education()
        self.input_major(addResModel_data['cus_major'])
        self.input_intent(addResModel_data['cus_intent'])
        self.select_workage()
        self.input_salary(addResModel_data['cus_salary'])
        self.select_source()
        self.input_applposition(addResModel_data['cus_applposition'])
        self.input_age(addResModel_data['cus_age'])
        self.input_eduexp(addResModel_data['cus_eduexp'])
        self.input_experience(addResModel_data['cus_experience'])
        self.input_last_tracking(addResModel_data['cus_last_tracking'])
        self.click_save_button()

    #点击上传专属
    def click_upload_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(8)').click()

    # 选择区域
    def select_region2(self):
        region_select = self.driver.find_element_by_name('regionSelect')
        Service.select_random(region_select)

    #选择部门
    def select_dept(self):
        dept_select = self.driver.find_element_by_name('dpetSelect')
        Service.select_random(dept_select)

    #选择文件
    def select_files(self,files_path):
        self.driver.find_element_by_id('files').send_keys(files_path)

    #点击提交按钮
    def click_submit_button(self):
        self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()

    def upload_files(self,base_config_path, upload_files_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.market()
        self.click_upload_button()
        self.select_region2()
        self.select_dept()
        self.select_files(upload_files_data['files_path'])

    #点击读取邮箱
    def read_email_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(7)').click()

    #点击确定
    def read_ok_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()

    #读取邮箱动作组织
    def read_email(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.second_password('..\\config\\base.conf')
        self.market()
        self.read_email_button()
        self.read_ok_button()


if __name__ == '__main__':
    driver=webdriver.Firefox()













