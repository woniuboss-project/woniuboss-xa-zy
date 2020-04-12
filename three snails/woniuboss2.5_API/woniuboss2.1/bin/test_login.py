from woniuboss2.lib.login import Login
from woniuboss2.tools.utility import Utility

class LoginTest:
    def __init__(self,data_config_path):
        self.data_config_info = Utility.get_json(data_config_path)

    def test_login(self):
        #准备数据
        login_info=Utility.get_excel_to_dict(self.data_config_info[0])
        for info in login_info:
            login_url=info['URL']
            login_data=info['DATA']
            login_resp = Login().do_login(login_url, login_data)
            #将返回的正文当做预期结果
            login_resp_content=login_resp.text
            #断言
            flag=Utility.assert_equals(login_resp_content,info['CONTENT'])
            if flag:
                print('login test pass')
            else:
                print('login test fail')

if __name__ == '__main__':
    LoginTest('..\\config\\testdata.conf').test_login()