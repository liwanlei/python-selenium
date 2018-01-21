# -*- coding: utf-8 -*-
# @Author  : leizi
from base.blo import Zaohui_tes
import yaml,unittest,time,os
from util import log
from selenium import webdriver
path=os.getcwd()
class Testzhaohui(unittest.TestCase):
    def setUp(self):
        title=u'找回密码测试'
        self.logs=log.log_message(title)
        self.derve=webdriver.Firefox()
        self.data_file = open(path+"\\page\\lo_data.yaml","r",encoding= "utf-8")
        self.data = yaml.load(self.data_file)
        self.data_file.close()
        self.zhaohui_data=self.data['zhaohui']
        self.zhaohui_fun=Zaohui_tes(self.derve)
    def test_zhaohui_1(self):
        try:
            self.username=self.data['zhaohui_data_1']['username']
            self.email=self.data['zhaohui_data_1']['email']
            self.suc=self.data['zhaohui_data_1']['suc']
            self.assert_vale=self.data['zhaohui_data_1']['assert_vale']
            self.retu_data=self.zhaohui_fun.zhaohui(self.username,self.email,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhaohui1.png')
            self.logs.info_log('inptut name:%s,email:%s,assert:%s'%(self.username,self.email,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.retu_data, self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def test_zhaohui_2(self):
        try:
            self.username=self.data['zhaohui_data_2']['username']
            self.email=self.data['zhaohui_data_2']['email']
            self.suc=self.data['zhaohui_data_2']['suc']
            self.assert_vale=self.data['zhaohui_data_2']['assert_vale']
            self.retu_data=self.zhaohui_fun.zhaohui(self.username,self.email,self.suc)
            self.derve.get_screenshot_as_file(path+'\\jietu\\zhaohui2.png')
            self.logs.info_log('inptut name:%s,email:%s,assert:%s'%(self.username,self.email,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.retu_data, self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def tearDown(self):
        self.derve.quit()
if __name__=="__main__":
    unittest.main()