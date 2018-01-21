# -*- coding: utf-8 -*-
# @Author  : leizi
from base.blo import Zhuce_tes
import yaml,unittest,time,os
from util import log
from selenium import webdriver
path=os.getcwd()
class Testzhuce(unittest.TestCase):
    def setUp(self):
        title=u'注册测试'
        self.logs=log.log_message(title)
        self.derve=webdriver.Firefox()
        self.data_file = open(path+"\\page\\lo_data.yaml","r",encoding= "utf-8")
        self.data = yaml.load(self.data_file)
        self.data_file.close()
        self.zhuce_data=self.data['zhuce']
        self.zhuce_fun=Zhuce_tes(self.derve)
    def test_zhuce_1(self):
        try:
            self.name=self.zhuce_data['zhuce_data_1']['username']
            self.password=self.zhuce_data['zhuce_data_1']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_1']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_1']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_1']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_1']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_1']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce1.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_2(self):
        try:
            self.name=self.zhuce_data['zhuce_data_2']['username']
            self.password=self.zhuce_data['zhuce_data_2']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_2']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_2']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_2']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_2']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_2']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce2.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_3(self):
        try:
            self.name=self.zhuce_data['zhuce_data_3']['username']
            self.password=self.zhuce_data['zhuce_data_3']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_3']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_3']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_3']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_3']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_3']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce3.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_4(self):
        try:
            self.name=self.zhuce_data['zhuce_data_4']['username']
            self.password=self.zhuce_data['zhuce_data_4']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_4']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_4']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_4']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_4']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_4']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce4.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_5(self):
        try:
            self.name=self.zhuce_data['zhuce_data_5']['username']
            self.password=self.zhuce_data['zhuce_data_5']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_5']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_5']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_5']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_5']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_5']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce5.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_6(self):
        try:
            self.name=self.zhuce_data['zhuce_data_6']['username']
            self.password=self.zhuce_data['zhuce_data_6']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_6']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_6']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_6']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_6']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_6']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce6.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_7(self):
        try:
            self.name=self.zhuce_data['zhuce_data_7']['username']
            self.password=self.zhuce_data['zhuce_data_7']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_7']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_7']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_7']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_7']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_7']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhuce7.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def tearDown(self):
        self.derve.quit()
if __name__=="__main__":
    unittest.main()