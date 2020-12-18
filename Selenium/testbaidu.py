import unittest
from selenium import webdriver
import time

class TestCase(unittest.TestCase):
    def setUp(self):
        self.web = webdriver.Chrome()
        self.web.implicitly_wait(10)
        self.url = "https://www.baidu.com"    

    def test_case1(self):
        web = self.web
        web.get(self.url)
        web.find_element_by_id("kw").send_keys("软件测试")
        web.find_element_by_id("su").click()
        time.sleep(3)
        

    def tearDown(self):
        self.web.quit()

if __name__ == "__main__":
    unittest.main()