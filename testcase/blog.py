# -*- coding: utf-8 -*-
# @Time    : 2017/8/11 20:57
# @Author  : lileilei
# @Site    : 
# @File    : blog.py
# @Software: PyCharm
import  unittest
from base.py_se import PySele
url='https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'
dir=PySele(brower='Chrome')
class BlogTest(unittest.TestCase):
    def setUp(self):
        global url
        dir.open(url)
    def testLogin(self):
        dir.send_key('id','input1','leizi')
        dir.send_key('id','input2','liwanlei')
        dir.clic('id','signin')
        me=dir.element('id','signin').text
        self.assertEqual(me,'登录',msg='用户名或者密码错误')
    def tearDown(self):
        dir.kill()
if __name__=='__mian__':
    unittest.main()
