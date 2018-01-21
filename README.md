# python+selenium +HTMLTestRunner+yaml自动化
## python 3 +selenium2 +HTMLTestRunner(python3版本)
### 使用的框架是python自带的unittest。

### base 文件来放着对Login_tes，Zhuce_tes，Zaohui_tes等类的封装，我在case只要调用这里面的类传入相应的参数就可以。
###  testcase用来放置测试用例的地方，我写了几个用例文件，每个用例的命名是为了让我以后可以更好的查代码，
## paged用来放数据的，包括页面的定位的数据，还有测试用例所用的数据，(注：这里使用yaml文件是因为python很好解析该类文件)
### jietu汉语的字面意思，我在运行测试用例的时候。我需要截图的地方，利用selenium自动的截图功能来截取，(这里命名一定要与测试用例相对应)
### lo 放置log。同样我也吧log模块的简单封装放到这里
### report 这里放置的是测试报告，我吧执行的测试用例的一个脚本放在这里。我可以在命令行直接运行
### testsuite  组织测试的suite
### util 公共模块
###  run.py运行的注模块