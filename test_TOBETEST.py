import unittest
from TOBETEST import *

class TestTobetest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5,add(2,3))
        self.assertEqual(5, add(5,6))

    def test_minus(self):
        self.assertEqual(4,minus(6,2))
        self.assertEqual(5,minus(5,1))


    def setUp(self):
        print("每个测试用例（test开头的方法）  前 运行一次-准备基础数据")
        a=5
        b=8

    def tearDown(self):
        print("每个测试用例（test开头的方法） 结束后 运行一次-清理数据还原现场")

    @classmethod
    def setUpClass(self):
        print("class 结束后 运行一次-清理数据还原现场")

    @classmethod
    def tearDownClass(self):
        print("class 结束后 运行一次-清理数据还原现场")

if __name__ =="__main__":
    unittest.main(verbosity=1)