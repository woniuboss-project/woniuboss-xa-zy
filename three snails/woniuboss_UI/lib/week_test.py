#周考成绩
import os
from time import sleep
from woniuboss_UI.tools.service import Service
class Weekgrade:
#=================================封装动作=================================================
#查询，选择区域
    def select_area(self,driver,value):
        area_ele = "/html/body/div[8]/div[2]/div/div/div/div[1]/select[1]"
        area = driver.find_element_by_xpath(area_ele)
        Service.select_value(area,value)
#查询，选择班级
    def select_class(self,driver,value):
        # 选择班级名
        cname_ele = "/html/body/div[8]/div[2]/div/div/div/div[1]/select[2]"
        cname = driver.find_element_by_xpath(cname_ele)
        Service.select_value(cname,value)
#查询，填写姓名
    def input_name(self,driver,value):
        name_ele = "/html/body/div[8]/div[2]/div/div/div/div[1]/input"
        name = driver.find_element_by_xpath(name_ele)
        Service.send_input(name, value)
#查询按钮
    def btn_query(self,driver):
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/button").click()
#周考导入按钮
    def btn_upload_weekgrade(self,driver):
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/div/button[2]").click()
    # 周考导入，选择班级
    def btn_upload_class(self,driver,value):
        upload_class_ele = "import_cl"
        upload_class = driver.find_element_by_id(upload_class_ele)
        Service.select_value(upload_class,value)
    # 周考导入，选择阶段
    def btn_upload_stage(self,driver,value):
        upload_stage_ele = "import_ph"
        upload_stage = driver.find_element_by_id(upload_stage_ele)
        Service.select_value(upload_stage,value)
    # 周考导入，选择周数
    def btn_upload_week(self,driver,value):
        upload_week_ele = "import_we"
        upload_week = driver.find_element_by_id(upload_week_ele)
        Service.select_value(upload_week,value)
    # 周考导入，上传文件
    def btn_upload_file(self,driver,value):
        btn_upload_file=driver.find_element_by_xpath('//*[@id="files"]')
        filepath = os.path.join(os.getcwd(), 'week_grade.xlsx')
        btn_upload_file.send_keys(filepath)
    # 周考导入的提交按钮
    def btn_upload_submission(self,driver):
        driver.find_element_by_css_selector(".modal-lg > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()
    # 周考导入按钮
    def btn_upload(self,driver):
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/div/button[2]").click()

    # 查看模板
    def view_template(self,driver):
        driver.find_element_by_css_selector("div.pull-right:nth-child(5) > button:nth-child(1) > a:nth-child(1)").click()
    #数据导出，btn_download
    def data_export(self,driver):
        driver.find_element_by_id("btn_download")
    #上传返回的确定按钮
    def upload_resp_btn(self,driver):
        driver.find_element_by_css_selector(".bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()

    # 上传返回的确定按钮
    def upload_resp(self, driver):
        upload_resp=driver.find_element_by_css_selector(".bootbox-body").text
        return upload_resp
    #周考记录录入
    def btn_record_entry_input(self,driver):
     Service.get_random_btn(driver)

    #周考记录录入中的班级选项
    def record_entry_class(self,driver,value):
        record_entry_class=driver.find_element_by_id("we_cl")
        Service.select_value(record_entry_class,value)
    # 周考记录录入中的班级选项，we_phase
    def record_entry_stage(self,driver,value):
        record_entry_stage=driver.find_element_by_id("we_phase")
        Service.select_value(record_entry_stage,value)
    #周考记录录入中的周数选项，we_week
    def record_entry_weeks(self,driver,value):
        record_entry_weeks=driver.find_element_by_id("we_week")
        Service.select_value(record_entry_weeks,value)
    #周考记录录入中的输入框：分数
    def record_entry_grade(self,driver,value):
        record_entry_grade=driver.find_element_by_xpath("/html/body/div[9]/div/div/div[2]/form/div[2]/div[4]/input")
        Service.send_input(record_entry_grade,value)
    #周考记录录入中的保存按钮
    def record_entry_keep(self, driver):
        driver.find_element_by_xpath("/html/body/div[9]/div/div/div[3]/button").click()
    #加号
    def btn_plus(self,driver):
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[1]/a/i").click()
    #修改阶段成绩
    def edit_grade(self,driver,value):
        edit_grade=driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/div[1]/div[2]/div[2]/table/tbody/tr/td[3]")
        Service.send_input(edit_grade,value)
    #修改阶段成绩提交按钮
    def edit_btn(self,driver):
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td/div[1]/div[2]/div[2]/table/tbody/tr/td[9]/button").click()

#=====================================动作整合==================================================
#数据导出按钮
    def btn_data_export(self,driver):
        driver.find_element_by_id("btn_download").click()
#周考成绩查询整合
    def week_grade_query(self,driver,week_query_data):
        self.select_area(driver,week_query_data[0])
        self.select_class(driver,week_query_data[1])
        self.input_name(driver,week_query_data[2])
        self.btn_query(driver)

#周考导入整合
    def week_grade_upload(self,driver,week_upload_data):
        print(week_upload_data)
        print(week_upload_data[3])
        self.btn_upload(driver)
        self.btn_upload_class(driver,week_upload_data[0])
        self.btn_upload_stage(driver,week_upload_data[1])
        self.btn_upload_week(driver,week_upload_data[2])
        self.btn_upload_file(driver,week_upload_data[3])
        self.btn_upload_submission(driver)

#周考记录录入整合
    def record_entry(self,driver,record_entry_data):
        self.btn_record_entry_input(driver)
        self.record_entry_class(driver,record_entry_data[0])
        self.record_entry_stage(driver,record_entry_data[1])
        self.record_entry_weeks(driver,record_entry_data[2])
        sleep(2)
        self.record_entry_grade(driver,record_entry_data[3])
        sleep(3)
        self.record_entry_keep(driver)

#修改阶段考成绩
    def edit_test_grade(self,driver,edit_data):
        self.btn_plus(driver)
        sleep(2)
        self.edit_grade(driver,int(edit_data))
        sleep(2)
        self.edit_btn(driver)
        sleep(2)