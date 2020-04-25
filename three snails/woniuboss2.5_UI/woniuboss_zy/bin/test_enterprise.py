import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from woniuboss.lib.enterprise_customer import Enterprise
from woniuboss.tools.service import Service
from woniuboss.tools.utility import Utility


test_config_info = Utility.get_json('..\\config\\testdata.conf')
add_enterprise_info = Utility.get_excel_to_tuple(test_config_info[4])
edit_enterprise_info = Utility.get_excel_to_tuple(test_config_info[5])
search_enterprise_info = Utility.get_excel_to_tuple(test_config_info[6])

class EnterpriseTest(unittest.TestCase):

	def setUp(self):
		self.driver = Service.get_driver('..\\config\\base.conf')
		self.enterprise = Enterprise(self.driver)

	def tearDown(self):
		self.driver.quit()

	@parameterized.expand(add_enterprise_info)
	def test_add_enterprise(self, Nentername, Nentercate, Naddress, Nname,number,mail,QQ,expect):
		add_enterprise_data = {'newentname': Nentername, 'newentcate': Nentercate,
							 'address': Naddress,'header':Nname,'phonenumber':number,'e_mail':mail,'qq':QQ}
		# 添加之前检查企业的总数
		sql = 'select count(enterprise_id) from enterprise_info'
		old_enterprise_count = Utility.query_one('..\\config\\base.conf', sql)
		# 执行添加企业的操作
		self.enterprise.add_enterprise('..\\config\\base.conf', add_enterprise_data)
		# 对添加动作的结果进行验证
		if Service.is_element_present(self.driver, By.CSS_SELECTOR,'button.btn-padding:nth-child(1)'):
			time.sleep(2)
			# 用于获取弹出页面的文本内容
			content = self.driver.find_element_by_css_selector('#enterpriseTb > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(1)').text
			if '蜗牛学院' in content:
				new_enterprise_count = Utility.query_one('..\\config\\base.conf', sql)
				if new_enterprise_count[0] - old_enterprise_count[0] == 1:
					actual = 'add-success'
				else:
					actual = 'add-fail'
			else:
				actual = 'add-fail'
		else:
			actual = 'add-fail'
		self.assertEqual(actual, expect)

	@parameterized.expand(edit_enterprise_info)
	def test_edit_enterprise(self, enterprise_name, enterprise_cate, expect):
		edit_enterprise_data = {'entName': enterprise_name, 'entcate': enterprise_cate}
		# 修改之前检查企业的名称，所属行业
		sql = 'select ent_name,ent_category from enterprise_info where enterprise_id = 1'
		old_enterprise_info = Utility.query_one('..\\config\\base.conf', sql)
		# 执行修改企业的操作
		self.enterprise.edit_enterprise('..\\config\\base.conf', edit_enterprise_data)
		new_enterprise_info = Utility.query_one('..\\config\\base.conf', sql)
		if Service.is_element_present(self.driver, By.CSS_SELECTOR,'button.btn-padding:nth-child(1)'):
			time.sleep(2)
			# 用于获取弹出页面的文本内容
			content = self.driver.find_element_by_css_selector('#enterpriseTb > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)').text
			if '中软国际' in content:
				if new_enterprise_info != old_enterprise_info:
					actual = 'edit-success'
				else:
					actual = 'edit-fail'
			else:
				actual = 'edit-fail'
		else:
			actual = 'edit-fail'
		self.assertEqual(actual, expect)

	@parameterized.expand(search_enterprise_info)
	def test_search_enterprise(self,employee_name,expect):
		search_enterprise_data = {'employee': employee_name}
		#执行搜索操作
		self.enterprise.search('..\\config\\base.conf', search_enterprise_data)
		if WebDriverWait(self.driver, 5, 1).until(
				lambda dr: dr.find_element(By.XPATH,'//table[@id="enterpriseTb"]/tbody/tr[1]/td[1]').text) == employee_name:
			actual = 'query-pass'
		else:
			actual = 'query-fail'
		self.assertEqual(actual,expect)