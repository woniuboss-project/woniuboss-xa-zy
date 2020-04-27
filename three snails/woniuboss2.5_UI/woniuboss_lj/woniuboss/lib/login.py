from woniuboss.tools.service import Service


class Login:
    def __init__(self, driver):
        self.driver = driver

    # 向用户名输入框输入内容
    def input_uname(self, username):
            uname = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[1]/input')
            Service.send_input(uname, username)

    # 向密码框输入密码
    def input_upass(self, password):
        upass = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[2]/input')
        Service.send_input(upass, password)

    # 向验证码框输入验证码
    def input_code(self, verification):
        ucode = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div/div[3]/input')
        Service.send_input(ucode, verification)

    # 点击登录按钮
    def click_button(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()

    # 将以上的动作进行组织，形成整体的登录操作,参数login_data是字典
    def do_login(self, base_config_path, login_data):
        Service.open_page(self.driver, base_config_path)
        self.input_uname(login_data['username'])
        self.input_upass(login_data['password'])
        # self.input_code(login_data['verification'])
        self.click_button()