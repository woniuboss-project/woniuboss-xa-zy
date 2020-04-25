import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By

from woniuboss.lib.financial_manage import FinancialManage
from woniuboss.tools.service import Service
from woniuboss.tools.utility import Utility

test_config_info = Utility.get_json('..\\config\\testdata.conf')
add_flow_info = Utility.get_excel_to_tuple(test_config_info[1])
add_password_info = Utility.get_excel_to_tuple(test_config_info[9])

class FinancialTest(unittest.TestCase):

	def setUp(self):
		self.driver = Service.get_driver('..\\config\\base.conf')
		self.financial = FinancialManage(self.driver)

	def tearDown(self):
		self.driver.quit()

	@parameterized.expand(add_flow_info)
	def test_add_flow(self, money, countparty, record, expect):
		add_flow_data = {'moneyNo': money, 'counterpartyName': countparty,
							 'textarea': record}
		#新增之前检查流水的总数
		sql = 'select count(detailed_id) from detailed_dealings'
		old_flow_count = Utility.query_one('..\\config\\base.conf', sql)
		# 执行添加流水的操作
		self.financial.add_flow('..\\config\\base.conf', add_flow_data)
		# 对添加动作的结果进行验证
		if Service.is_element_present(self.driver, By.CSS_SELECTOR,'button.btn:nth-child(10)'):
			time.sleep(2)
			# 用于获取弹出页面的文本内容
			content = self.driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/div/div/div[1]/div[4]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[13]/button').text
			if '修改' in content:
				actual = 'add-success'
			else:
				actual = 'add-fail'
		else:
			# 判断表中的记录数是否增加
			new_flow_count = Utility.query_one('..\\config\\base.conf', sql)
			if new_flow_count[0] - old_flow_count[0] == 1:
				actual = 'add-success'
			else:
				actual = 'add-fail'

		self.assertEqual(actual, expect)

	#二次解密
	@parameterized.expand(add_password_info)
	def test_twice_decrypt(self, t_word, expect):
		add_password_data = {'password':t_word}
		#执行解密动作
		self.financial.decrypt('..\\config\\base.conf', add_password_data)
		if Service.is_element_present(self.driver, By.CSS_SELECTOR, '.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)'):
			content = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div').text
			if '错误' in content:
				actual = 'decrypt-fail'
			else:
				actual = 'no-decrypt'
		else:
			actual = 'decrypt-success'
		self.assertEqual(actual,expect)