from woniuboss.tools.service import Service
import time

class Enterprise:
    def __init__(self,driver):
        self.driver = driver

    #点击新增企业按钮
    def click_add_enterprise(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/button[1]').click()

    #输入企业名称
    def input_entname(self,newentname):
        ename = self.driver.find_element_by_id('newentname')
        Service.send_input(ename,newentname)

    #输入所属行业
    def input_entcate(self,newentcate):
        ecate = self.driver.find_element_by_id('newentcate')
        Service.send_input(ecate,newentcate)

    #输入企业地址
    def input_address(self,address):
        addr = self.driver.find_element_by_id('newentaddr')
        Service.send_input(addr,address)

    #输入联系人
    def input_header(self,header):
        hname = self.driver.find_element_by_id('newentheader')
        Service.send_input(hname,header)

    #输入联系电话
    def input_number(self,phonenumber):
        number = self.driver.find_element_by_id('newtel')
        Service.send_input(number,phonenumber)

    #输入邮箱
    def input_main(self,e_mail):
        mail = self.driver.find_element_by_id('newemail')
        Service.send_input(mail,e_mail)

    #输入QQ
    def input_qq(self,qq):
        QQ = self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/div/form/div[7]/input')
        Service.send_input(QQ,qq)

    #点击“添加”按钮
    def click_add(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div/div/div[3]/button').click()

    #新增企业
    def add_enterprise(self,base_config_path,add_enterprise_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[4]').click()
        time.sleep(6)
        self.click_add_enterprise()
        self.input_entname(add_enterprise_data['newentname'])
        self.input_entcate(add_enterprise_data['newentcate'])
        self.input_address(add_enterprise_data['address'])
        self.input_header(add_enterprise_data['header'])
        self.input_number(add_enterprise_data['phonenumber'])
        self.input_main(add_enterprise_data['e_mail'])
        self.input_qq(add_enterprise_data['qq'])
        self.click_add()
        driver.switch_to.alert.accept()

    #点击“修改”按钮
    def click_edit(self):
        self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[7]/button').click()

    # 修改企业名称
    def edit_employee_name(self,entName):
        employee_name = self.driver.find_element_by_id('entName')
        Service.send_input(employee_name,entName)

    # 修改所属行业
    def edit_entcate(self, entcate):
        cate = self.driver.find_element_by_id('entCate')
        Service.send_input(cate, entcate)

    #修改后点击“保存”按钮
    def click_esave(self):
        self.driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/button').click()

    #修改企业
    def edit_enterprise(self,base_config_path,edit_enterprise_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[4]').click()
        time.sleep(6)
        self.click_edit()
        self.edit_employee_name(edit_enterprise_data['entName'])
        self.edit_entcate(edit_enterprise_data['entcate'])
        self.click_esave()
        #driver.switch_to.alert.accept()

    #输入企业名称
    def input_employee_name(self,employee):
        emoloyeename = self.driver.find_element_by_name('companyName')
        Service.send_input(emoloyeename,employee)

    #点击搜索按钮
    def click_search(self):
        self.driver.find_element_by_xpath('//div[@id="content"]/div[2]/div[1]/button[2]').click()

    #搜索企业
    def search(self,base_config_path,search_enterprise_data):
        driver = self.driver
        Service.miss_login(driver, base_config_path)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[4]').click()
        time.sleep(6)
        self.input_employee_name(search_enterprise_data['employee'])
        self.click_search()