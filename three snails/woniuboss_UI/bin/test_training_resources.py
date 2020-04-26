
import unittest
from selenium import webdriver
from woniuboss_UI.lib.Training_resources import Training_Resources
from woniuboss_UI.lib.login import Login
from woniuboss_UI.tools.utility  import Utility
from parameterized import parameterized
exlce = '../data/WoniuBoss_info.xlsx'
#获取excel文件内容
data = Utility.get_excel_to_dict(exlce,'培训资源',1,6,3,4)
login_data = Utility.get_excel_to_dict(exlce,'login',1,2,3,4)

#赋值并且传参
class Test_train(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #调用地址
        cls.driver.get('http://192.168.1.113:8080/WoniuBoss4.0')
        #调用模块
        #登陆
        Login().do_login(cls.driver,login_data)
        Training_Resources().tranin(cls.driver)
    @parameterized.expand(data)
    def test_one(self,data):
        Training_Resources().all_opration(self.driver,data)
        try :
            name = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[1]').text
        except :
            actual = 'fail'
        else :
            if name == data['姓名']:
                actual = 'success'
            else :
                actual = 'fail'
        self.assertEquals(actual,data['expect'])
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)
