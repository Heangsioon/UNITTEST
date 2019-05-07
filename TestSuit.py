import unittest
from test_TOBETEST import *

suit=unittest.TestSuite()
testcasesss=[TestTobetest('test_add'),TestTobetest('test_minus')]
suit.addTests(testcasesss)
runner=unittest.TextTestRunner(verbosity=2)
runner.run(suit)