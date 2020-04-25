from woniuboss_4.tools.service import Service
from selenium.webdriver.support.select import Select

class Stage_Evaluate:

    def __init__(self,driver):
        self.driver = driver

    # 解密
    def solve_password(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        password = self.driver.find_element_by_name('secondPass')
        Service.send_input(password, 'woniu123')
        self.driver.find_element_by_css_selector('#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    # 点击学员管理按钮
    def click_student_manage(self):
        self.driver.find_element_by_link_text('学员管理').click()

    #点击阶段考评
    def click_stage(self):
        self.driver.find_element_by_link_text('阶段考评').click()

    #点击录入按钮
    def click_import(self):
        self.driver.find_element_by_css_selector('#pe-result > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(9) > button:nth-child(1)').click()

    #选择班级
    def choose_grade(self,grade):
        Select(self.driver.find_element_by_id('ph_cl')).select_by_visible_text(grade)

    #录入成绩
    def input_score(self,score):
        new_score = self.driver.find_element_by_name('ph.newscore')
        Service.send_input(new_score,score)

    #选择阶段
    def choose_stage(self,stage):
        Select(self.driver.find_element_by_id('ph_phase')).select_by_visible_text(stage)

    #点击保存按钮
    def click_save_btn(self):
        self.driver.find_element_by_css_selector('#phaseExam-modal > div > div > div.modal-footer > button').click()

    #录入阶段考动作组合
    def import_score(self,base_config_path,stage_score_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_student_manage()
        self.click_stage()
        self.solve_password()
        self.click_import()
        self.choose_grade(stage_score_data['grade'])
        self.input_score(stage_score_data['score'])
        self.choose_stage(stage_score_data['stage'])
        self.click_save_btn()

    #点击阶段导入按钮
    def click_stage_import(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()

    #选择班级
    def choose_Grade(self,Grade):
        Select(self.driver.find_element_by_id('import_cl')).select_by_visible_text(Grade)

    #选择阶段
    def choose_Stage(self,Stage):
        Select(self.driver.find_element_by_id('import_ph')).select_by_visible_text(Stage)

    #选择文件
    def choose_file(self,file_path):
        file = self.driver.find_element_by_css_selector('#files')
        Service.send_input(file,file_path)

    #点击提交按钮
    def click_submit_button(self):
        self.driver.find_element_by_css_selector('#upRes-modal > div > div > div.modal-footer > button').click()

    #阶段导入动作组合
    def import_stage(self,base_config_path,import_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_student_manage()
        self.click_stage()
        self.solve_password()
        self.click_stage_import()
        self.choose_Grade(import_data['Grade'])
        self.choose_Stage(import_data['Stage'])
        self.choose_file(import_data['file_path'])
        self.click_submit_button()

