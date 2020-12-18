import unittest
from test_case import test_baidu
from test_case import test_youdao

suite = unittest.TestSuite()
suite.addTest(test_baidu.TestBaidu("test_baidu"))
suite.addTest(test_youdao.TestYouDao("test_youdao"))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)