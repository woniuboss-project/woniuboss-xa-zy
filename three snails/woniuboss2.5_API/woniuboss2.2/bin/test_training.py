#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from parameterized import parameterized
from woniuboss2.tools.utility import Utility
from woniuboss2.lib.training import Tran
# 获取测试数据
data_config_info = Utility.get_json('..\\config\\testdata.conf')
query_message_info=Utility.get_excel_to_tuple(data_config_info[1])
query_resume_info=Utility.get_excel_to_tuple(data_config_info[2])
Track_resources_info=Utility.get_excel_to_tuple(data_config_info[3])
Modify_information_info=Utility.get_excel_to_tuple(data_config_info[4])
add_information_info=Utility.get_excel_to_tuple(data_config_info[5])
transfer_query_info=Utility.get_excel_to_tuple(data_config_info[6])
transfer_view_info=Utility.get_excel_to_tuple(data_config_info[7])
transfer_commit_info=Utility.get_excel_to_tuple(data_config_info[8])
distribution_query_info=Utility.get_excel_to_tuple(data_config_info[9])
Proportionate_distribution_info=Utility.get_excel_to_tuple(data_config_info[10])
Public_query_info=Utility.get_excel_to_tuple(data_config_info[11])
Public_claim_info=Utility.get_excel_to_tuple(data_config_info[12])
class TestTrain(unittest.TestCase):
    def setUp(self):
        def setUp(self):
            print("test start")

        def tearDown(self):
            print("test end")
    #搜索功能
    @parameterized.expand(query_message_info)
    def test_query_message(self, query_message_url,post, query_message_data, status_code,content):
        training_query_message_resp = Tran().query_message(query_message_url, query_message_data)
        actual = training_query_message_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(query_resume_info)
    def test_query_resume(self, query_resume_url, post, query_resume_data, status_code, content):
        training_query_resume_resp = Tran().query_resume(query_resume_url, query_resume_data)
        actual = training_query_resume_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(Track_resources_info)
    def test_Track_resources(self, Track_resources_url, post, Track_resources_data, status_code, content):
        training_Track_resources_resp = Tran().Track_resources(Track_resources_url, Track_resources_data)
        actual = training_Track_resources_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(Modify_information_info)
    def test_Modify_information(self, Modify_information_url, post, Modify_information_data, status_code, content):
        training_Modify_information_resp = Tran().Modify_information(Modify_information_url, Modify_information_data)
        actual = training_Modify_information_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(add_information_info)
    def test_add_information(self, add_information_url, post, add_information_data, status_code, content):
        training_add_information_resp = Tran().add_information(add_information_url, add_information_data)
        actual = training_add_information_resp.text
        # 断言
        self.assertEqual(actual, content)


    @parameterized.expand(transfer_query_info)
    def test_transfer_query(self, transfer_query_url, post, transfer_query_data, status_code, content):
        training_transfer_query_resp = Tran().transfer_query(transfer_query_url, transfer_query_data)
        actual = training_transfer_query_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(transfer_view_info)
    def test_transfer_view(self, transfer_view_url, post, transfer_view_data, status_code, content):
        training_transfer_view_resp = Tran().transfer_view(transfer_view_url, transfer_view_data)
        actual = training_transfer_view_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(transfer_commit_info)
    def test_transfer_commit(self, transfer_commit_url, post, transfer_commit_data, status_code, content):
        training_transfer_commit_resp = Tran().transfer_commit(transfer_commit_url, transfer_commit_data)
        actual = training_transfer_commit_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(distribution_query_info)
    def test_distribution_query(self, distribution_query_url, post, distribution_query_data, status_code, content):
        training_distribution_query_resp = Tran().distribution_query(distribution_query_url, distribution_query_data)
        actual = training_distribution_query_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(Proportionate_distribution_info)
    def test_Proportionate_distribution(self, Proportionate_distribution_url, post, Proportionate_distribution_data, status_code, content):
        training_Proportionate_distribution_resp = Tran().Proportionate_distribution(Proportionate_distribution_url, Proportionate_distribution_data)
        actual = training_Proportionate_distribution_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(Public_query_info)
    def test_Public_query(self, Public_query_url, post, Public_query_data,status_code, content):
        training_Public_query_resp = Tran().Public_query(Public_query_url,Public_query_data)
        actual = training_Public_query_resp.text
        # 断言
        self.assertEqual(actual, content)

    @parameterized.expand(Public_claim_info)
    def test_Public_claim(self, Public_claim_url, post, Public_claim_data,status_code, content):
        training_Public_claim_resp = Tran().Public_query(Public_claim_url,Public_claim_data)
        actual = training_Public_claim_resp.text
        # 断言
        self.assertEqual(actual, content)




if __name__ == '__main__':
    unittest.main(verbosity=2)


