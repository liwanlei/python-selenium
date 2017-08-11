# -*- coding: utf-8 -*-
# @Author  : leizi
from bl.blo import Zhuce_tes
import yaml,unittest,time
from lo import log
from selenium import webdriver
class Testzhuce(unittest.TestCase):
    def setUp(self):
        title=u'注册测试'
        self.logs=log.log_message(title)
        self.derve=webdriver.Firefox()
        self.data_file = open(r"C:\Users\Administrator\Desktop\te_blogf\data\lo_data.yaml","r",encoding= "utf-8")
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce1.png')
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce2.png')
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce3.png')
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce4.png')
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce5.png')
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce6.png')
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
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce7.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_8(self):
        try:
            self.name=self.zhuce_data['zhuce_data_8']['username']
            self.password=self.zhuce_data['zhuce_data_8']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_8']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_8']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_8']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_8']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_8']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce8.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_9(self):
        try:
            self.name=self.zhuce_data['zhuce_data_9']['username']
            self.password=self.zhuce_data['zhuce_data_9']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_9']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_9']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_9']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_9']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_9']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce9.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_10(self):
        try:
            self.name=self.zhuce_data['zhuce_data_10']['username']
            self.password=self.zhuce_data['zhuce_data_10']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_10']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_10']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_10']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_10']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_10']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce10.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def test_zhuce_11(self):
        try:
            self.name=self.zhuce_data['zhuce_data_11']['username']
            self.password=self.zhuce_data['zhuce_data_11']['mima']
            self.passwordque=self.zhuce_data['zhuce_data_11']['nima2']
            self.shoujihao=self.zhuce_data['zhuce_data_11']['shoujihao']
            self.youxiang=self.zhuce_data['zhuce_data_11']['youxiang']
            self.suc=self.zhuce_data['zhuce_data_11']['suc']
            self.assert_vale=self.zhuce_data['zhuce_data_11']['assert_vale']
            self.re_data=self.zhuce_fun.zhuce(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.suc)
            self.derve.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\te_blogf\jietu\zhuce11.png')
            self.logs.info_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(self.name,self.password,self.passwordque,self.shoujihao,self.youxiang,self.assert_vale))
            time.sleep(1)
            self.assertEqual(self.re_data, self.assert_vale)

        except Exception as e:
            self.logs.error_log(e)
    def tearDown(self):
        self.derve.quit()
if __name__=="__main__":
    unittest.main()