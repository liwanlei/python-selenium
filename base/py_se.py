from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class PySele():
	def __init__(self,brower):#初始化浏览器
		if brower =='firefox' or brower =='Firefox' or brower =='f' or brower =='F':
			deriver=webdriver.Firefox()
		elif brower =='Ie' or brower =='ie' or brower =='i' or brower=='I':
			deriver=webdriver.Ie()
		elif brower =='Chrome' or brower =='chrome' or brower =='Ch' or brower=='ch':
			deriver=webdriver.Chrome()
		elif brower =='PhantomJS' or brower =='phantomjs' or brower =='ph' or brower=='phjs':
			deriver=webdriver.PhantomJS()
		elif brower =='Edge' or brower =='edge' or brower =='Ed' or brower=='ed':
			deriver=webdriver.Edge()
		elif brower =='Opera' or brower =='opera' or brower =='op' or brower=='OP':
			deriver=webdriver.Opera()
		elif brower =='Safari' or brower =='safari' or brower =='sa' or brower=='saf':
			deriver=webdriver.Safari()
		else:
			raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
		self.driver=deriver
	def element(self,fangfa,dingwei):#定位
		if fangfa=='id':
			element=self.driver.find_element_by_id(dingwei)
		elif fangfa == "name":
			element = self.driver.find_element_by_name(dingwei)
		elif fangfa == "class":
			element = self.driver.find_element_by_class_name(dingwei)
		elif fangfa == "link_text":
			element = self.driver.find_element_by_link_text(dingwei)
		elif fangfa == "xpath":
			element = self.driver.find_element_by_xpath(dingwei)
		elif fangfa == "tag":
			element = self.driver.find_element_by_tag_name(dingwei)
		elif fangfa == "css":
			element = self.driver.find_element_by_css_selector(dingwei)
		else:
			raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
		return element
	def elements(self,fangfa,dingwei):#组定位
		if fangfa=='id':
			element=self.driver.find_elements_by_id(dingwei)
		elif fangfa == "name":
			element = self.driver.find_elements_by_name(dingwei)
		elif fangfa == "class":
			element = self.driver.find_elements_by_class_name(dingwei)
		elif fangfa == "link_text":
			element = self.driver.find_elements_by_link_text(dingwei)
		elif fangfa == "xpath":
			element = self.driver.find_elements_by_xpath(dingwei)
		elif fangfa == "tag":
			element = self.driver.find_elements_by_tag_name(dingwei)
		elif fangfa == "css":
			element = self.driver.find_elements_by_css_selector(dingwei)
		else:
			raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
		return element
	def element_wait(self,fangfa,dingwei,wati=6):#等待
		if fangfa == "id":
			WebDriverWait(self.driver,wati,1).until(EC.presence_of_element_located((By.ID, dingwei)))
		elif fangfa == "name":
			WebDriverWait(self.driver,wati,1).until(EC.presence_of_element_located((By.NAME, dingwei)))
		elif fangfa == "class":
			WebDriverWait(self.driver,wati,1).until(EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
		elif fangfa == "link_text":
			WebDriverWait(self.driver,wati,1).until(EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
		elif fangfa == "xpath":
			WebDriverWait(self.driver,wati,1).until(EC.presence_of_element_located((By.XPATH, dingwei)))
		elif fangfa == "css":
			WebDriverWait(self.driver,wati,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
		else:
			raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")
	def open(self,url):#打开网页
		self.driver.get(url)
	def make_maxwindow(self):#最大化浏览器
		self.driver.maximize_window()
	def set_winsize(self,wide,hight):#设置窗口
		self.driver.set_window_size(wide,hight)
	def send_key(self,fangfa,dingwei,text):#发送内容
		self.element(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		e1.clear()
		e1.send_keys(text)
	def clear(self,fangfa,dingwei):#清空
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		e1.clear()
	def clic(self,fangfa,dingwei):#单击
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		e1.click()
	def right_click(self,fangfa,dingwei):#右击
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		ActionChains(self.driver).context_click(e1).perform()
	def move_element(self,fangfa,dingwei):#移动到
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		ActionChains(self.driver).move_to_element(e1).perform()
	def double_click(self,dingwei,fangfa):#双击
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		ActionChains(self.driver).double_click(e1).perform()
	def  drag_and_drop(self,fangfa1,e1,fangfa2,e2):#从e1到e2
		self.element_wait(fangfa1,e1)
		eme1=self.element(fangfa1,e1)
		self.element_wait(fangfa2,e2)
		eme2=self.element(fangfa2,e2)
		ActionChains(self.driver).drag_and_drop(eme1,eme2).perform()
	def click_text(self,text):#点击文字
		self.driver.find_element_by_link_text(text).click()
	def close(self):#关闭
		self.driver.close()
	def kill(self):#退出
		self.driver.quit()
	def sublimit(self,fangfa,dingwei):#提交
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		e1.sublimit()
	def f5(self):#刷新
		self.driver.refresh()
	def js(self,sprit):#执行js
		self.driver.execute_script(sprit)
	def get_attribute(self, fangfa,dingwei, attribute):
		e1=self.element(fangfa,dingwei)
		return e1.get_attribute(attribute)
	def get_text(self,fangfa,dingwei):
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		return e1.text
	def get_is_dis(self,fangfa,dingwei):
		self.element_wait(fangfa,dingwei)
		e1=self.element(fangfa,dingwei)
		return e1.is_displayed()
	def get_title(self,fangfa,dingwei):#获取title
		return self.driver.title
	def get_screen(self,file_path):#截屏
		self.driver.get_screenshot_as_file(file_path)
	def wait(self,fangfa,dingwei):#等待
		self.driver.implicitly_wait((fangfa,dingwei))
	def accpet(self):#允许
		self.driver.switch_to.alert.accept()
	def dismiss_alert(self):
		self.driver.switch_to.alert.dismiss()
	def switch_to_frame(self, fangfa,dingwei):#切换
		self.element_wait(fangfa,dingwei)
		if1=self.element(fangfa,dingwei)
		self.driver.switch_to.frame(if1)