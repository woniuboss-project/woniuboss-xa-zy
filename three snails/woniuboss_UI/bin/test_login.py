import time,unittest
from parameterized import parameterized


# 获取登录用的测试信息
from woniuboss_UI.lib.login import Login
from woniuboss_UI.tools.service import Service
from woniuboss_UI.tools.utility import Utility

test_config_info = Utility.get_json('..\\config\\testdata.conf')
login_info = Utility.get_excel_to_tuple(test_config_info[0])


class LoginTest(unittest.TestCase):
	def __init__(self):
		self.driver = driver

	@classmethod
	def setUpClass(cls):
		cls.driver = Service.get_driver('..\\config\\base.conf')
		cls.login = Login(cls.driver)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	@parameterized.expand(login_info)
	def test_login(self,uname,upass,vfcode,expect):
		# 将参数重新组织成字典
		login_data = {'username':uname,'password':upass,'verification':vfcode}
		self.login.do_login('..\\config\\base.conf',login_data)
		from selenium.webdriver.common.by import By
		if Service.is_element_present(self.driver,By.LINK_TEXT,'注销'):
			actual = 'success'
			self.driver.find_element_by_link_text('注销').click()
		else:
			actual = 'fail'
			self.driver.refresh()
		self.assertEqual(actual,expect)