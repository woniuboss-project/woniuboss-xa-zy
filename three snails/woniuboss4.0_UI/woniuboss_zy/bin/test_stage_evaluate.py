import time
import unittest
from parameterized import parameterized
from selenium.webdriver.common.by import By

from woniuboss_4.lib.stage_evaluate import Stage_Evaluate
from woniuboss_4.tools.service import Service
from woniuboss_4.tools.utility import Utility

test_config_info = Utility.get_json('..\\config\\testdata.conf')
import_evaluate_info = Utility.get_excel_to_tuple(test_config_info[2])
import_stage_info = Utility.get_excel_to_tuple(test_config_info[3])

class StageTest(unittest.TestCase):
    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        self.stage = Stage_Evaluate(self.driver)

    def tearDown(self):
        self.driver.quit()

    @parameterized.expand(import_evaluate_info)
    def test_import_score(self,s_grade,s_score,s_stage,expect):
        stage_score_data = {'grade':s_grade,'score':s_score,'stage':s_stage}
        self.stage.import_score('..\\config\\base.conf',stage_score_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,'.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)'):
            actual = 'test-import-fail'
        else:
            actual = 'test-import-success'
        self.assertEqual(actual,expect)

    @parameterized.expand(import_stage_info)
    def test_import_stage(self, grade, stage, f_path, expect):
        import_data = {'Grade':grade,'Stage':stage,'file_path':f_path}
        self.stage.import_stage('..\\config\\base.conf',import_data)
        if Service.is_element_present(self.driver, By.CSS_SELECTOR,'.bootbox > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2)'):
            actual = 'test-import-fail'
        else:
            actual = 'test-import-success'
        self.assertEqual(actual,expect)