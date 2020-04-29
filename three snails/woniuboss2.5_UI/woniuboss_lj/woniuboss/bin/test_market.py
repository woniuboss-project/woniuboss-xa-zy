from selenium.webdriver.common.by import By

from woniuboss.tools.service import Service
from woniuboss.tools.utility import Utility
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 查询资源
test_qureyNetCus_info = Utility.get_excel_to_tuple(data_config_info[1])
# 新增资源
test_addCus_info = Utility.get_excel_to_tuple(data_config_info[2])
# 上传简历
test_validateUpload_info = Utility.get_excel_to_tuple(data_config_info[3])



class TestMarket(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver=Service.get_driver('..\\config\\base.conf')
        from woniuboss.lib.market import Market
        cls.market=Market(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    # 查询资源
    # @parameterized.expand(test_qureyNetCus_info)
    # def test_qureyNetCus(self,stime,etime,expect):
    #     qureyNetCus_data = {'stime':stime,'etime':etime}
    #     self.market.qureyNetCus('..\\config\\base.conf',qureyNetCus_data)
    #     if Service.is_element_present(self.driver,By.CSS_SELECTOR,'#netCus-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1) > div:nth-child(1)') or Service.is_element_present(self.driver,By.CSS_SELECTOR,'.no-records-found > td:nth-child(1)'):
    #         actual = 'query_successful'
    #     else:
    #         actual='query_failed'
    #     # 断言
    #     self.assertEqual(actual, expect)

    #默认查询
    def test_query_all(self):
        self.market.query_all('..\\config\\base.conf')
        if Service.is_element_present(self.driver,By.CSS_SELECTOR,'#netCus-table > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1) > div:nth-child(1)') or Service.is_element_present(self.driver,By.CSS_SELECTOR,'.no-records-found > td:nth-child(1)'):
            actual = 'query_successful'
        else:
            actual='query_failed'
        # 断言
        self.assertEqual(actual, 'query_successful')

    # # 新增资源
    # @parameterized.expand(test_addCus_info)
    # def test_addCus(self, cus_phone,cus_name, cus_email, cus_qq,cus_school,cus_major,cus_intent,cus_salary,cus_applposition,cus_age,cus_eduexp,cus_experience,cus_last_tracking,expect):
    #     addResModel_data={'cus_phone':cus_phone,'cus_name':cus_name,'cus_email':cus_email,'cus_qq':cus_qq,
    #                       'cus_school':cus_school,'cus_major':cus_major,'cus_intent':cus_intent,'cus_salary':cus_salary,
    #                       'cus_applposition': cus_applposition, 'cus_age': cus_age,'cus_eduexp':cus_eduexp,'cus_experience':cus_experience,
    #                       'cus_last_tracking': cus_last_tracking}
    #     self.market.addCus('..\\config\\base.conf', addResModel_data)
    #     if Service.is_element_present(self.driver,By.CSS_SELECTOR,'div.bootbox-body'):
    #         actual='add_successful'
    #     else:
    #         actual='add_successful'
    #     #断言
    #     self.assertEqual(actual,expect)

    # # 上传简历
    # @parameterized.expand(test_validateUpload_info)
    # def test_validateUpload(self,files_path,expect ):
    #     upload_files_data={'files_path':files_path}
    #     self.market.upload_files('..\\config\\base.conf',upload_files_data)
    #     if Service.is_element_present(self.driver,By.XPATH,'/html/body/div[9]/div/div/div[2]/div'):
    #         actual = 'upload_successful'
    #     else:
    #         actual='upload_failed'
    #     # 断言
    #     self.assertEqual(actual, expect)

    #读取邮箱
    def test_read_email(self):
        self.market.read_email('..\\config\\base.conf')
        if Service.is_element_present(self.driver,By.CSS_SELECTOR,'p.loading-title.txt-textOneRow'):
            actual = 'read_successful'
        else:
            actual='read_failed'
        # 断言
        self.assertEqual(actual, 'read_successful')

if __name__ == '__main__':
    unittest.main(verbosity=2)