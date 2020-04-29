from woniuboss4.tools.service import Service
import time
class Resource:

    def __init__(self,driver):
        self.driver=driver

    def decode(self):
        # 解密
        self.driver.find_element_by_css_selector('#btn-decrypt').click()
        self.driver.find_element_by_css_selector('div.modal-body:nth-child(2) > input:nth-child(1)').send_keys('woniu123')
        self.driver.find_element_by_css_selector('#secondPass-modal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #培训资源
    def resource_management(self):
        #点击资源管理，进入资源管理界面
        self.driver.find_element_by_css_selector('div.panel:nth-child(5) > div:nth-child(1) > a:nth-child(1)').click()

    #点击资源管理内的培训资源
    def tranin(self):
        self.driver.find_element_by_css_selector('#list-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()

    #选择资源库的下拉框
    def resource_store(self):
        Resource_bank= self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(1) > select:nth-child(1)')
        Service.select_random(Resource_bank)

    #选择状态的下拉框
    def select_status(self):
        state = self.driver.find_element_by_name('last_status')
        Service.select_random(state)

    #选择来源下拉框
    def select_source(self):
        source = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(1) > select:nth-child(3)')
        Service.select_random(source)

    # 选择区域下拉框
    def select_region(self):
        area = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(1)')
        Service.select_random(area)

    # 选择部门下拉框
    def select_department(self):
        department = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(2)')
        Service.select_random(department)

    # 选择咨询师下拉框
    def select_consultant(self):
        counselor = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(8) > select:nth-child(3)')
        Service.select_random(counselor)

    # 选择开始时间
    def select_begin(self,stime):
        Service.remove_readonly(self.driver, 'date1')
        stime_ele = self.driver.find_element_by_id('date1')
        Service.send_input(stime_ele, stime)

    # 选择结束时间
    def select_end(self,etime):
        Service.remove_readonly(self.driver, 'date2')
        etime_ele = self.driver.find_element_by_id('date2')
        Service.send_input(etime_ele, etime)

    # 选择姓名输入框
    def select_name(self,name):
        input_name = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(1) > input:nth-child(6)')
        Service.send_input(input_name, name)

    # 点击搜索按钮
    def click_search_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(7)').click()

    #搜索资源动作组织
    def query_resource(self,base_config_path, query_resource_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        time.sleep(3)
        self.tranin()
        self.resource_store()
        self.select_status()
        self.select_region()
        self.select_department()
        self.select_consultant()
        self.select_begin(query_resource_data['stime'])
        self.select_end(query_resource_data['etime'])
        self.select_name(query_resource_data['name'])
        self.click_search_button()
        time.sleep(5)



    #新增按钮
    def new_button(self):
        self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()

    #输入姓名
    def input_name(self,name):
        input_name=self.driver.find_element_by_css_selector('div.has-feedback:nth-child(2) > input:nth-child(2)')
        Service.send_input(input_name,name)

    #输入电话
    def input_tel(self,phone):
        input_phone=self.driver.find_element_by_css_selector('#addCus > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)')
        Service.send_input(input_phone, phone)

    # 选择最新状态下拉框
    def select_new_status(self):
        status = self.driver.find_element_by_css_selector('#addCus > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > select:nth-child(2)')
        Service.select_random(status)

    # 选择渠道来源下拉框
    def select_channel(self):
        ditch = self.driver.find_element_by_css_selector('#addCus > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > select:nth-child(2)')
        Service.select_random(ditch)

    def select_save(self):
        # 点击保存
        self.driver.find_element_by_css_selector('#addCusBtn').click()
        #点击弹窗确定
        self.driver.find_element_by_css_selector('.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)').click()

    #新增动作的组织
    def add_resource(self,base_config_path, add_resource_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        self.tranin()
        self.new_button()
        self.input_name(add_resource_data['name'])
        self.input_tel(add_resource_data['phone'])
        self.select_new_status()
        self.select_channel()
        self.select_save()

    #点击废弃查询
    def click_abandon_query(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(7)').click()

    #选择一条废弃信息
    def select_abandon_info(self):
        self.driver.find_element_by_name('btSelectItem').click()

    #点击废弃按钮
    def click_abandon_button(self):
        self.driver.find_element_by_id('abandon').click()

    #点击确认废弃按钮
    def click_sure_abandon(self):
        self.driver.find_element_by_css_selector('button.btn-primary:nth-child(2)').click()
    def abandon_resource(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        self.tranin()
        self.click_abandon_query()
        self.select_abandon_info()
        self.click_abandon_button()
        self.click_sure_abandon()
        time.sleep(3)

    # #分配资源
    # #点击分配资源
    # def allocation(self):
    #     self.driver.find_element_by_css_selector('#list-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()
    #
    # #选择渠道
    # def select_source(self):
    #     source = self.driver.find_element_by_name('source')
    #     Service.select_random(source)
    #
    # #搜索框输入
    # def input_info(self,info):
    #     input_info=self.driver.find_element_by_name('cusInfo')
    #     Service.send_input(input_info,info)
    #
    # #点击查询
    # def click_query_button(self):
    #     self.driver.find_element_by_css_selector('button.btn-info:nth-child(2)')


    #转交资源
    #点击资源管理内的转交资源
    def transfer(self):
        self.driver.find_element_by_css_selector('#list-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > a:nth-child(1)').click()

    # 选择区域下拉框
    def select_transfer_region(self):
        area = self.driver.find_element_by_id('regionSelect1')
        Service.select_random(area)

    #选择部门的下拉框
    def select_dept(self):
        dept= self.driver.find_element_by_name('dept')
        Service.select_random(dept)

    #选择咨询师的下拉框
    def select_emp(self):
        emp = self.driver.find_element_by_id('empNameSelect1')
        Service.select_random(emp)

    #选择来源下拉框
    def select_transfer_source(self):
        source = self.driver.find_element_by_name('source')
        Service.select_random(source)

    #搜索框输入
    def input_transfer_info(self,info):
        input_info=self.driver.find_element_by_name('cusInfo')
        Service.send_input(input_info,info)

    #点击查询
    def click_transfer_query_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(8)')

    #查询动作的组织
    def transfer_query(self,base_config_path,transfer_query_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        time.sleep(3)
        self.transfer()
        self.select_transfer_region()
        self.select_dept()
        self.select_emp()
        self.select_transfer_source()
        self.input_transfer_info(transfer_query_data['info'])
        self.click_transfer_query_button()
        time.sleep(5)

    #点击查看查询
    def click_look_query(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(8)').click()

    #点击查看
    def click_look_button(self):
        self.driver.find_element_by_css_selector('#transmit-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(14) > button:nth-child(1)').click()

    #查看动作的组织
    def look_resume(self,base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        time.sleep(2)
        self.transfer()
        time.sleep(2)
        self.click_look_query()
        self.click_look_button()
        time.sleep(3)

    #点击查询
    def click_turn_query_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(8)').click()

    #选择一条信息
    def select_info(self):
        self.driver.find_element_by_name('btSelectItem').click()

    # 选择区域下拉框
    def select_turn_region(self):
        area = self.driver.find_element_by_id('regionSelect2')
        Service.select_random(area)

    # 选择部门的下拉框
    def select_turn_dept(self):
        dept = self.driver.find_element_by_id('deptSelect2')
        Service.select_random(dept)

    # 选择咨询师的下拉框
    def select_turn_emp(self):
        emp = self.driver.find_element_by_id('empNameSelect2')
        Service.select_random(emp)

    #点击提交
    def click_commit(self):
        self.driver.find_element_by_id('Submit').click()

    #点击确认
    def click_sure_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()

    #转交资源动作组织
    def turn_resource(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        time.sleep(2)
        self.transfer()
        time.sleep(2)
        self.click_turn_query_button()
        self.select_info()
        self.select_turn_region()
        self.select_turn_dept()
        self.select_turn_emp()
        self.click_commit()
        self.click_sure_button()
        time.sleep(3)


    #公共资源
    #点击公共资源
    def click_common(self):
        self.driver.find_element_by_css_selector('#list-3 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)').click()

    # 选择区域下拉框
    def select_common_region(self):
        area = self.driver.find_element_by_name('region')
        Service.select_random(area)

    # 选择部门下拉框
    def select_common_department(self):
        department = self.driver.find_element_by_name('dept')
        Service.select_random(department)

    #选择废弃人下拉框
    def select_common_emp(self):
        emp= self.driver.find_element_by_name('empName')
        Service.select_random(emp)

    #选择状态的下拉框
    def select_common_status(self):
        state = self.driver.find_element_by_name('last_status')
        Service.select_random(state)

    #选择来源下拉框
    def select_common_source(self):
        source = self.driver.find_element_by_name('source')
        Service.select_random(source)

    # 选择学历下拉框
    def select_common_education(self):
        education = self.driver.find_element_by_name('education')
        Service.select_random(education)

    # 输入框输入
    def input_common_info(self,info):
        input_info = self.driver.find_element_by_name('cusInfo')
        Service.send_input(input_info, info)

    # 点击查询按钮
    def click_common_search_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(8)').click()

    #查询动作的组织
    def common_query(self, base_config_path,common_query_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        self.click_common()
        self.select_common_region()
        self.select_common_department()
        self.select_common_emp()
        self.select_common_status()
        self.select_common_source()
        self.select_common_education()
        self.input_common_info(common_query_data['info'])
        self.click_common_search_button()
        time.sleep(3)

    #点击认领查询按钮
    def click_claim_query_button(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(8)').click()

    #选择一条信息
    def click_claim_info(self):
        self.driver.find_element_by_name('btSelectItem').click()

    #点击认领
    def click_claim_button(self):
        self.driver.find_element_by_id('ownCusBtn').click()

    #点击确认
    def click_sure_claim(self):
        self.driver.find_element_by_css_selector('button.btn:nth-child(2)').click()

    #认领动作组织
    def claim_resource(self, base_config_path):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        self.decode()
        self.resource_management()
        self.click_common()
        self.click_claim_query_button()
        self.click_claim_info()
        self.click_claim_button()
        self.click_sure_claim()
        time.sleep(3)





