import unittest
if __name__=='__main__':
    suit=unittest.TestSuite()
    tests=unittest.defaultTestLoader.loadTestsFromNames(['test_TOBETEST.test_add','test_TOBETEST.test_minus'])
    suit.addTests(tests)
    #suit.addTests(unittest.【报错少了names 用default】TestLoader.loadTestsFromNames(['test_TOBETEST.test_add','test_TOBETEST.test_minus']))
    with open('report.txt','a') as f:
        runner=unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suit)