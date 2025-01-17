from selenium import webdriver
import unittest, time

class TestYouDao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://fanyi.youdao.com"
    
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("inputOriginal").send_keys("你好")
        driver.find_element_by_id("inputOriginal").submit()
        time.sleep(3)
        page_source = driver.page_source
        self.assertIn("hello", page_source)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

