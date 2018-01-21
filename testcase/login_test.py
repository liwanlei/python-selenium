from base.blo import Login_tes
import yaml,unittest,time
from util import  log
from selenium import webdriver
import  os
path=os.getcwd()
class Testlogin(unittest.TestCase):
    def setUp(self):
        title=u'登陆测试'
        self.logs=log.log_message(title)
        self.derve=webdriver.Firefox()
        self.data_file = open(path+"\\page\\lo_data.yaml","r",encoding= "utf-8")
        self.data = yaml.load(self.data_file)
        self.data_file.close()
        self.login_data=self.data["login"]
        self.login_fun=Login_tes(self.derve)
    def test_login1(self):
        try:
            self.name=self.login_data['login_data_1']['username']
            self.pwd=self.login_data['login_data_1']['pwd']
            self.suc=self.login_data['login_data_1']['suc']
            self.assert_value = self.login_data['login_data_1']['assert']
            self.derve.get_screenshot_as_file(path+'\\jietu\\login1.png')
            self.logs.info_log('input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.name, self.pwd, self.suc, self.assert_value))
            time.sleep(2)
            self.re_data = self.login_fun.login( self.suc,self.name, self.pwd)
            time.sleep(2)
            self.assertEqual(self.re_data, self.assert_value)
        except Exception as e:
            self.logs.error_log(e)
    def test_login2(self):
        try:
            self.name1=self.login_data['login_data_2']['username']
            self.pwd1=self.login_data['login_data_2']['pwd']
            self.suc1=self.login_data['login_data_2']['suc']
            self.assert_value1 = self.login_data['login_data_2']['assert']
            self.re_data1 = self.login_fun.login( self.suc1,self.name1, self.pwd1)
            self.derve.get_screenshot_as_file(path+'\\jietu\\login2.png')
            self.logs.info_log('input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.name1, self.pwd1, self.suc1, self.assert_value1))
            time.sleep(2)
            self.assertEqual(self.re_data1, self.assert_value1)
        except Exception as e:
            self.logs.error_log(e)
    def test_login3(self):
        try:
            self.name2=self.login_data['login_data_3']['username']
            self.pwd2=self.login_data['login_data_3']['pwd']
            self.suc2=self.login_data['login_data_3']['suc']
            self.assert_value2= self.login_data['login_data_3']['assert']
            self.re_data2 = self.login_fun.login( self.suc2,self.name2, self.pwd2)
            self.derve.get_screenshot_as_file(path+'\\jietu\\login3.png')
            self.logs.info_log(
                'input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.name2, self.pwd2, self.suc2, self.assert_value2))
            time.sleep(2)
            self.assertEqual(self.re_data2, self.assert_value2)
        except Exception as e:
            self.logs.error_log(e)
    def tearDown(self):
        self.derve.quit()
