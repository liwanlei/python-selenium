# -*- coding: utf-8 -*-
# @Author  : leizi
from base.blo import Xiugai_tes
from selenium import webdriver
import yaml,unittest,time,os
from util import log
path=os.getcwd()
class Test_xiugai(unittest.TestCase):
    def setUp(self):
        title=u'修改密码测试'
        self.logs=log.log_message(title)
        self.derve=webdriver.Firefox()
        self.data_file = open(path+"\\page\\lo_data.yaml","r",encoding= "utf-8")
        self.data = yaml.load(self.data_file)
        self.data_file.close()
        self.xiugai_data=self.data['xiugai']
        self.xiugai_fun=Xiugai_tes(self.derve)
    def test_xiugai_1(self):
        try:
            self.password=self.xiugai_data['xiugai_data_1']['yuanmi']
            self.xiugaimi=self.xiugai_data['xiugai_data_1']['xiugaimi']
            self.xiugaimi1=self.xiugai_data['xiugai_data_1']['xiugaimi1']
            self.suc=self.xiugai_data['xiugai_data_1']['suc']
            self.assert_vale=self.xiugai_data['xiugai_data_1']['assert_vale']
            self.return_data=self.xiugai_fun.xiugai(self.suc,self.password,self.xiugaimi,self.xiugaimi1)
            self.logs.info_log("input: password:%s,xiugaimima:%s,xiugaimima1:%s,assert:%s"%(self.password,self.xiugaimi,self.xiugaimi1,self.assert_vale))
            time.sleep(1)
            self.assertAlmostEqual(self.return_data,self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def test_xiugai_2(self):
        try:
            self.password=self.xiugai_data['xiugai_data_2']['yuanmi']
            self.xiugaimi=self.xiugai_data['xiugai_data_2']['xiugaimi']
            self.xiugaimi1=self.xiugai_data['xiugai_data_2']['xiugaimi1']
            self.suc=self.xiugai_data['xiugai_data_2']['suc']
            self.assert_vale=self.xiugai_data['xiugai_data_2']['assert_vale']
            self.return_data=self.xiugai_fun.xiugai(self.suc,self.password,self.xiugaimi,self.xiugaimi1)
            self.derve.get_screenshot_as_file(path+'\\jietu\\xiugai2.png')
            self.logs.info_log("input: password:%s,xiugaimima:%s,xiugaimima1:%s,assert:%s"%(self.password,self.xiugaimi,self.xiugaimi1,self.assert_vale))
            time.sleep(1)
            self.assertAlmostEqual(self.return_data,self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def test_xiugai_3(self):
        try:
            self.password=self.xiugai_data['xiugai_data_3']['yuanmi']
            self.xiugaimi=self.xiugai_data['xiugai_data_3']['xiugaimi']
            self.xiugaimi1=self.xiugai_data['xiugai_data_3']['xiugaimi1']
            self.suc=self.xiugai_data['xiugai_data_3']['suc']
            self.assert_vale=self.xiugai_data['xiugai_data_3']['assert_vale']
            self.return_data=self.xiugai_fun.xiugai(self.suc,self.password,self.xiugaimi,self.xiugaimi1)
            self.derve.get_screenshot_as_file(path+'\\jietu\\xiugai3.png')
            self.logs.info_log("input: password:%s,xiugaimima:%s,xiugaimima1:%s,assert:%s"%(self.password,self.xiugaimi,self.xiugaimi1,self.assert_vale))
            time.sleep(1)
            self.assertAlmostEqual(self.return_data,self.assert_vale)
        except Exception as e:
            self.logs.error_log(e)
    def tearDown(self):
        self.derve.quit()
