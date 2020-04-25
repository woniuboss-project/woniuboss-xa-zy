from selenium.webdriver.support.select import Select
from woniuboss_4.tools.service import Service


class Student_info:

    def __init__(self,driver):
        self.driver = driver

    #解密
    def solve_password(self):
        self.driver.find_element_by_id('btn-decrypt').click()
        password = self.driver.find_element_by_name('secondPass')
        Service.send_input(password,'woniu123')
        self.driver.find_element_by_css_selector('#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #点击学员管理按钮
    def click_student_manage(self):
        self.driver.find_element_by_link_text('学员管理').click()

    #点击学员信息按钮
    def click_student_info(self):
        self.driver.find_element_by_link_text('学员信息').click()

    #选择方向
    def choose_direction(self,direction):
        Select(self.driver.find_element_by_name('orientation')).select_by_visible_text(direction)

    #选择班级
    def choose_class(self,classname):
        Select(self.driver.find_element_by_name('stuClass')).select_by_visible_text(classname)

    #选择状态
    def choose_status(self,status):
        Select(self.driver.find_element_by_name('stuStatus')).select_by_visible_text(status)

    #输入姓名
    def choose_name(self,name):
        Select(self.driver.find_element_by_name('stuName')).select_by_visible_text(name)

    #点击搜索按钮
    def click_search(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(10)').click()

    #执行搜索动作组合
    def search_action(self,base_config_path,search_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_student_manage()
        self.click_student_info()
        self.solve_password()
        self.choose_direction(search_data['direction'])
        self.choose_class(['classname'])
        self.choose_status(['status'])
        self.choose_name(['name'])
        self.click_search()

    #点击修改按钮
    def click_modify_button(self):
        self.driver.find_element_by_css_selector('#stuInfo_table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(12) > button:nth-child(2)').click()

    #选择最新状态
    def choose_new_status(self,newstatus):
        Select(self.driver.find_element_by_name('stu.status')).select_by_visible_text(newstatus)

    #选择应缴学费
    def choose_tuition(self,tuition):
        Select(self.driver.find_element_by_name('stu.need_fee')).select_by_visible_text(tuition)

    #输入QQ
    def input_qq(self,qq):
        QQ = self.driver.find_element_by_name('stu.QQ')
        Service.send_input(QQ,qq)

    #输入联系人
    def input_contacts(self,ContactName):
        name = self.driver.find_element_by_name('stu.emergency_person')
        Service.send_input(name,ContactName)

    #输入紧急电话
    def input_telephone(self,phonenumber):
        phone = self.driver.find_element_by_name('stu.emergency_tel')
        Service.send_input(phone,phonenumber)

    #点击保存按钮
    def click_save_button(self):
        self.driver.find_element_by_css_selector('#form-modify > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #修改学员基本信息
    def edit_stuinfo(self,base_config_path,student_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.click_student_manage()
        self.click_student_info()
        self.solve_password()
        self.click_search()
        self.click_modify_button()
        self.choose_new_status(student_data['newstatus'])
        self.choose_tuition(student_data['tuition'])
        self.input_qq(student_data['qq'])
        self.input_contacts(student_data['ContactName'])
        self.input_telephone(student_data['phonenumber'])
        self.click_save_button()

    # #点击日常考评
    # def click_daily_test(self):
    #     self.driver.find_element_by_link_text('日常考评').click()
    #
    # #点击
    # def select_homework_level(self, level):
    #     Select(self.driver.find_element_by_xpath('//*[@id="4"]/tbody/tr[1]/td[9]/select[1]')).select_by_visible_text(level)
    #
    # def click_work_btn(self):
    #     ele = self.driver.find_element_by_css_selector('#confirmAttenBtn_1')
    #     ele.click()
    #     return ele.get_attribute('onclick')
    #
    # def do_click_homework_btn(self, base_config_path,homework_data):
    #     driver = self.driver
    #     Service.miss_login(driver, base_config_path)
    #     self.click_student_manage()
    #     self.click_daily_test()
    #     self.select_homework_level(homework_data['level'])
    #     attr = self.click_work_btn()
    #     return attr


