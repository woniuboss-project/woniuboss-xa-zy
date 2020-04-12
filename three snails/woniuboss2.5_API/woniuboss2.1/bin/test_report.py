from woniuboss2.lib.report import Report
from woniuboss2.tools.utility import Utility
import unittest
from parameterized import parameterized

# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
# 咨询部数据
test_console_info = Utility.get_excel_to_tuple(data_config_info[21])
# 电销部数据
test_sale_info = Utility.get_excel_to_tuple(data_config_info[22])
# 市场部数据
test_mark_info = Utility.get_excel_to_tuple(data_config_info[23])
# 就业部数据
test_job_info = Utility.get_excel_to_tuple(data_config_info[24])


class TestReport(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    # 咨询部报表中心功能测试
    @parameterized.expand(test_console_info)
    def test_console(self, console_url, post,console_data, status_code,content):
        console_resp = Report().console(console_url, console_data)
        actual = console_resp.text
        # 断言
        self.assertEqual(actual, content)

    # 电销部报表中心功能测试
    @parameterized.expand(test_sale_info)
    def test_sale(self, sale_url, post,sale_data, status_code,content):
        sale_resp = Report().sale(sale_url, sale_data)
        actual = sale_resp.text
        # 断言
        self.assertEqual(actual, content)

    # 市场部报表中心功能测试
    @parameterized.expand(test_mark_info)
    def test_mark(self, mark_url, post,mark_data, status_code,content):
        mark_resp = Report().mark(mark_url, mark_data)
        actual = mark_resp.text
        # 断言
        self.assertEqual(actual, content)

    # 就业部报表中心功能测试
    @parameterized.expand(test_job_info)
    def test_job(self, job_url, post,job_data, status_code,content):
        job_resp = Report().job(job_url, job_data)
        actual = job_resp.text
        # 断言
        self.assertEqual(actual, content)


if __name__ == '__main__':
    unittest.main(verbosity=2)
