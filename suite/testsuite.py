import  unittest,time,os
from util import BSTestRunner
from config import description,reporttitle
path=os.getcwd()
case_path=path+'\\case'
def create_report():
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern='*test.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)
    now=time.strftime('%Y-%m-%d_%H_%M',time.localtime(time.time()))
    report_dir=path+'\\report\\%s.html'%now
    re_open= open(report_dir,'wb')
    runner=BSTestRunner.BSTestRunner(stream=re_open,title=reporttitle,description=description)
    runner.run(test_suit)
