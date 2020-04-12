from woniuboss2.tools.utility import Utility
from woniuboss2.lib.market import Market
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 查询资源
test_qureyNetCus_info = Utility.get_excel_to_tuple(data_config_info[18])
# 新增资源
test_addCus_info = Utility.get_excel_to_tuple(data_config_info[19])
# 上传简历
test_validateUpload_info = Utility.get_excel_to_tuple(data_config_info[20])



class TestMarket(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    # 新增资源
    @parameterized.expand(test_addCus_info)
    def test_addCus(self, addCus_url,post, addCus_data, status_code,content):
        market_add_resp = Market().addCus(addCus_url, addCus_data)
        actual = market_add_resp
        # 断言
        self.assertEqual(actual, content)

    # 上传简历
    @parameterized.expand(test_validateUpload_info)
    def test_validateUpload(self, validateUpload_url, post,validateUpload_data,status_code, content):
        validateUpload_resp = Market().validateUpload(validateUpload_url, validateUpload_data)
        actual = validateUpload_resp.text
        # 断言
        self.assertEqual(actual, content)

    # 查询资源
    @parameterized.expand(test_qureyNetCus_info)
    def test_qureyNetCus(self,qureyNetCus_url,post, qureyNetCus_data, status_code,content):
        qureyNetCus_resp = Market().qureyNetCus(qureyNetCus_url, qureyNetCus_data)
        actual = qureyNetCus_resp.text
        # 断言
        self.assertEqual(actual, content)


if __name__ == '__main__':
    unittest.main(verbosity=2)