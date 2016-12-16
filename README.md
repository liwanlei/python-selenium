# python+selenium +HTMLTestRunner+yaml自动化
python 3 +selenium2 +HTMLTestRunner(python3版本)
使用的框架是python自带的unittest。
通过类的封装等知识来进行自动化测试，本文的网站是基于我的博客的文章来写的，由于
自己是刚接触的selenium2，自己就大概看下别人的代码就来写这个的测试的用例，摸索的
前进，其中也遇到很多的坑。

bl文件来放着对Login_tes，Zhuce_tes，Zaohui_tes等类的封装，我在case只要调用这里面的类
传入相应的参数就可以。 我吧HTMLTestRunner也放在这个目录内。
case用来放置测试用例的地方，我写了几个用例，每个用例的命名是为了让我以后可以更好的查
代码，
data用来放数据的，包括页面的定位的数据，还有测试用例所用的数据，(注：这里使用yaml文件是因为python很好解析
该类文件)
jietu汉语的字面意思，我在运行测试用例的时候。我需要截图的地方，利用selenium自动的截图功能来截取，
(这里命名一定要与测试用例相对应)
lo 放置log。同样我也吧log模块的简单封装放到这里
report 这里放置的是测试报告，我吧执行的测试用例的一个脚本放在这里。我可以在命令行直接运行
python email_report.py 就可以直接运行脚本，运行完成后并且自动发送测试报告给相应的人。
 这个测试知识针对于单线程的测试。