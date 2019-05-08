import unittest
from test_TOBETEST import TestTobetest
from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner

if __name__ =="__main__":
    suit = unittest.TestSuite()
    suit.addTest(TestTobetest('test_add'))
    suit.addTest(TestTobetest('test_minus'))
    # 方式2
    # 测试用例均使用"test_"开头命名
    #test_dir='./'
    #suites = unittest.defaultTestLoader.discover(test_dir, 'test_TOBETEST.py', top_level_dir=test_dir)
    #方式3
    #tests = unittest.defaultTestLoader.loadTestsFromNames(['test_TOBETEST.test_add', 'test_TOBETEST.test_minus'])
    #suit.addTests(tests)
    with open("./report.html",'wb') as f:
        runner=HTMLTestRunner(stream=f,title="html_report",description="localhost login test",verbosity=2)
        runner.run(suit)