import yaml,os
path=os.getcwd()
from util import log
class Login_tes:#登录模块封装
    def __init__(self,driver):#
        self.driber=driver
        self.logs = log.log_message()
        self.file=open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
        self.data=yaml.load(self.file)
        self.file.close()
        self.lo_url=self.data['login'].get('url')
        self.denglu=self.data['login'].get('denglu')
        self.username=self.data['login'].get('name')
        self.password=self.data['login'].get('password')
        self.sub=self.data['login'].get('denglu_btm')
        self.lo_err=self.data['login'].get('login_err')
        self.lo_suc=self.data['login'].get('login_suc')
        self.driber.get(self.lo_url)
    def login(self,suc,name,password):
        try:
            self.driber.find_element_by_link_text(self.denglu).click()
            self.driber.find_element_by_id(self.username).clear()
            self.driber.find_element_by_id(self.username).send_keys(name)
            self.driber.find_element_by_id(self.password).click()
            self.driber.find_element_by_id(self.password).send_keys(password)
            self.driber.find_element_by_id(self.sub).click()
            if suc=='1':
                 self.login_su = self.driber.find_element_by_xpath(self.lo_suc).text
                 return self.login_su
            if suc=='0':
                self.login_err=self.driber.find_element_by_xpath(self.lo_err).text
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s'%e)
        finally:
            self.driber.quit()
class Zhuce_tes:#注册模块的封装
    def __init__(self,driver):
        self.deriver=driver
        title = '注册模块'
        self.logs = log.log_message()
        self.file1=open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
        self.data=yaml.load(self.file1)
        self.file1.close()
        self.zhu_url=self.data['zhuce'].get('url')
        self.zhu=self.data['zhuce'].get('zhuc')
        self.zhu_user=self.data['zhuce'].get('username')
        self.zhu_pwd=self.data['zhuce'].get('password')
        self.zhu_qpwd=self.data['zhuce'].get('querenpass')
        self.zhu_shouji=self.data['zhuce'].get('shouji')
        self.zhu_email=self.data['zhuce'].get('youxiang')
        self.zhu_butn=self.data['zhuce'].get('tijiao_btn')
        self.zhu_suc=self.data['zhuce'].get('zhuce_suc')
        self.zhu_err=self.data['zhuce'].get('zhuce_err')
        self.deriver.get(self.zhu_url)
    def zhuce(self,suc,name,password,password1,shouji,email):
        try:
            self.deriver.find_element_by_link_text(self.zhu).click()
            self.deriver.find_element_by_class_name(self.zhu_user).clear()
            self.deriver.find_element_by_class_name(self.zhu_user).send_keys(name)
            self.deriver.find_element_by_class_name(self.zhu_pwd).clear()
            self.deriver.find_element_by_class_name(self.zhu_pwd).send_keys(password)
            self.deriver.find_element_by_class_name(self.zhu_qpwd).clear()
            self.deriver.find_element_by_class_name(self.zhu_qpwd).send_keys(password1)
            self.deriver.find_element_by_class_name(self.zhu_shouji).clear()
            self.deriver.find_element_by_class_name(self.zhu_shouji).send_keys(shouji)
            self.deriver.find_element_by_class_name(self.zhu_email).clear()
            self.deriver.find_element_by_class_name(self.zhu_email).send_keys(email)
            self.deriver.find_element_by_class_name(self.zhu_butn).click()
            if suc =="1":
                self.zhu_su=self.deriver.find_element_by_id(self.zhu_suc).text
                return self.zhu_su
            if suc=='0':
                self.zhu_e=self.deriver.find_element_by_xpath(self.zhu_err).text
                return self.zhu_e
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s' % e)
        finally:
            self.deriver.quit()
class Zaohui_tes:
    def __init__(self,driver):
        self.driver=driver
        self.logs = log.log_message()
        self.file1=open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
        self.data=yaml.load(self.file1)
        self.file1.close()
        self.zhao_url=self.data['zhaohui'].get('url')
        self.zhao_username=self.data['zhaohui'].get('username')
        self.zhao_btn=self.data['zhaohui'].get('zhaohui_btn')
        self.zhao_err=self.data['zhaohui'].get('zhaohui_err')
        self.zhao_suc=self.data['zhaohui'].get('zhaohui_suc')
        self.driver.get(self.zhao_url)
    def zhaohui(self,suc,name,eamil):
        try:
            self.driver.find_element_by_css_selector(self.zhao_username).clear()
            self.driver.find_element_by_css_selector(self.zhao_username).sned_keys(name)
            self.driver.find_element_by_css_selector(self.zhao_eamil).clear()
            self.driver.find_element_by_css_selector(self.zhao_eamil).sned_keys(eamil)
            self.driver.find_element_by_css_selector(self.zhao_btn).click()
            if suc == '1':
                self.zhao_su=self.driver.find_element_by_css_selector(self.zhao_suc).text
                return self.zhao_su
            if suc =="0":
                self.zhao_er=self.driver.find_element_by_xpath(self.zhao_err).text
                return self.zhao_er
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s' % e)
        finally:
            self.driver.quit()
class Rest_tes:
    def __init__(self,driver):
        self.driver=driver
        self.logs = log.log_message()
        self.file1=open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
        self.data=yaml.load(self.file1)
        self.file1.close()
        self.rest_url=self.data['reset_pwd'].get('url')
        self.rest_eamil=self.data['reset_pwd'].get('email')
        self.reset_yan=self.data['reset_pwd'].get('yanzheng')
        self.reset_mima=self.data['reset_pwd'].get('mima')
        self.reset_mimaque=self.data['reset_pwd'].get('chongzhimima')
        self.reset_btn=self.data['reset_pwd'].get('reset_btn')
        self.reset_error=self.data['reset_pwd'].get('reset_error')
        self.reset_suc=self.data['reset_pwd'].get('reset_suc')
        self.driver.get(self.rest_url)
    def rest(self,suc,yan,eamil,mima,chongzhimima):
        try:
            self.driver.find_element_by_css_selector(self.rest_eamil).clear()
            self.driver.find_element_by_css_selector(self.rest_eamil).sned_keys(eamil)
            self.driver.find_element_by_css_selector(self.reset_yan).clear()
            self.driver.find_element_by_css_selector(self.reset_yan).sned_keys(yan)
            self.driver.find_element_by_css_selector(self.reset_mima).clear()
            self.driver.find_element_by_css_selector(self.reset_mima).sned_keys(mima)
            self.driver.find_element_by_css_selector(self.reset_mimaque).clear()
            self.driver.find_element_by_css_selector(self.reset_mimaque).sned_keys(chongzhimima)
            self.driver.find_element_by_css_selector(self.reset_btn).click()
            if suc =="1":
                self.rest_su=self.driver.find_element_by_id(self.reset_suc).text
                return self.rest_su
            if suc=='0':
                self.rest_err=self.driver.find_element_by_xpath(self.reset_error).text
                return self.rest_err
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s' % e)
        finally:
            self.driver.quit()
class Xiugai_tes:
    def __init__(self,driver):
        title = '修改模块'
        self.logs = log.log_message()
        self.driver=driver
        self.file1=open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
        self.data=yaml.load(self.file1)
        self.file1.close()
        self.xiugai_url=self.data['xiugai'].get('url')
        self.xiugai_yuan=self.data['xiugai'].get('yuanmi')
        self.xiugai_mima=self.data['xiugai'].get('xiugaimi')
        self.xiugai_mimaque=self.data['xiugai'].get('xiugaimi1')
        self.xiugai_btn=self.data['xiugai'].get('xiugai_but')
        self.xiugai_suc=self.data['xiugai'].get('xiu_suc')
        self.xiugai_error=self.data['xiugai'].get('xiu_err')
        self.driver.get(self.xiugai_url)
    def xiugai(self,suc,yuanmima,mima,querenmima):
        try:
            self.driver.find_element_by_css_selector(self.xiugai_yuan).clear()
            self.driver.find_element_by_css_selector(self.xiugai_yuan).sned_keys(yuanmima)
            self.driver.find_element_by_css_selector(self.xiugai_mima).clear()
            self.driver.find_element_by_css_selector(self.xiugai_mima).sned_keys(mima)
            self.driver.find_element_by_css_selector(self.xiugai_mimaque).clear()
            self.driver.find_element_by_css_selector(self.xiugai_mimaque).sned_keys(querenmima)
            self.driver.find_element_by_link_text(self.xiugai_btn).click()
            if suc=='1':
                 self.xiugai_su = self.driver.find_element_by_id(self.xiugai_suc).text
                 return self.xiugai_su
            if suc=='0':
                self.xiugai_erro=self.driver.find_element_by_xpath(self.xiugai_error).text
                return self.xiugai_erro
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s' % e)
        finally:
            self.driver.quit()