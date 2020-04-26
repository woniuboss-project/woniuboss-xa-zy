from selenium import webdriver
from woniuboss_UI.tools.utility import Utility
class Service:
    # 判断页面上的某个元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):

        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 向文本输入框执行三个固定操作：点击、清理、输入
    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    # 随机选择下拉框中的一项
    @classmethod
    def select_random(cls, selecter):  # selecter是传递的下拉框元素
        from selenium.webdriver.support.select import Select
        seleter_length = len(Select(selecter).options)
        import random
        random_index = random.randint(0, seleter_length - 1)
        Select(selecter).select_by_index(random_index)

    # 去掉某个元素的只读属性（id）
    @classmethod
    def remove_readonly(cls, driver, ele_id):
        driver.execute_script('document.getElementById("%s").readOnly=false' % (ele_id))

    # 具体的业务功能需要绕过登录，使用cookie
    @classmethod
    def miss_login(cls, driver, base_config_path):
        cls.open_page(driver, base_config_path)
        # 通过字典方式传递cookie信息
        contents = Utility.get_json(base_config_path)
        driver.add_cookie({'name': 'username', 'value': contents['username']})
        driver.add_cookie({'name': 'password', 'value': contents['password']})
        driver.add_cookie({'name': 'token', 'value': contents['token']})
        driver.add_cookie({'name': 'workId', 'value': contents['workId']})
        cls.open_page(driver, base_config_path)

    # 打开页面的方法
    @classmethod
    def open_page(cls, driver, base_config_path):
        contents = Utility.get_json(base_config_path)
        URL = 'http://%s:%s/%s' % (contents['HOSTNAME'], contents['PORT'], contents['AURL'])
        driver.get(URL)

    # 截图.仅进行截图操作
    @classmethod
    def get_png(cls, driver, png_path):
        driver.get_screenshot_as_file(png_path)

    # 出现缺陷后的截图方法
    @classmethod
    def get_error_png(cls, driver):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        png_path = '..\\bugpng\\error_%s.png' % (ctime)
        cls.get_png(driver, png_path)

    # 生成driver
    @classmethod
    def get_driver(cls, base_config_path):
        contents = Utility.get_json(base_config_path)
        from selenium import webdriver
        driver = getattr(webdriver, contents['BROWSER'])()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver


    @classmethod
    def select_value(cls,what,value):
        from selenium.webdriver.support.select import Select
        Select(what).select_by_visible_text(value)

    @classmethod
    def open_page(cls):
        driver = webdriver.Firefox()
        driver.get('http://192.168.1.113:8080/WoniuBoss2.5/')
        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.set_page_load_timeout(120)
        return driver

 # 随机获取页面上的列表中的按钮元素
    @classmethod
    def get_random_btn(cls,driver):
        #得到周考成绩记录数
        weeks=driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]")
        weeks_index=weeks.text
        w=weeks_index.strip().split("，")[0]
        print(w)
        a=w.split(" ")[-2]
        print(a)
        from random import randint
        random_num = randint(0, int(a))
        print(random_num)
        # 获取页面上所有的按钮元素
        btns=driver.find_element_by_xpath(f"html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{random_num}]/td[9]/button")

        #
        btns.click()