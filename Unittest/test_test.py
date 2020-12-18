# coding = utf-8
"""
Created on 2020-09-14
@author:alyssa

"""
import unittest
class BaiduTest(unittest.TestCase):

    # 定义setUp()方法用于测试用例执行前的初始化工作
    def setUp(self):
        self.number = input("Enter a number: ")
        self.number = int(self.number)

    # 定义测试用例，以“test_”开头命名的方法
    def test_case1(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg="Your input is not 10")

    def test_case2(self):
        print(self.number)
        self.assertEqual(self.number, 20, msg="Your input is not 20")

    @unittest.skip("暂时跳过用例3的测试")
    def test_case3(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg="Your input is not 30")

    def tearDown(self):
        print("Test over")

if __name__ == "__main__":
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(Test("test_case2"))
    # suite.addTest(Test("test_case1"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    test_dir = "D:/Python/unittest"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(discover)



    