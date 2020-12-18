import unittest
import HTMLTestRunner
import os
from Testsuite_baidu import BaiduUnittest
from Testsuite_baidu2 import BaiduUnittest2

unittest_tests = unittest.TestLoader().loadTestsFromTestCase(BaiduUnittest)
unittest_tests2 = unittest.TestLoader().loadTestsFromTestCase(BaiduUnittest2)
smoke_tests = unittest.TestSuite([unittest_tests, unittest_tests2])

unittest.TextTestRunner(verbosity=2).run(smoke_tests)

with open(dir + "/smokereport.html", "wb") as outfile:
    runner = HTMLTestRunner


