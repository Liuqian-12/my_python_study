import unittest
import time
from selenium import webdriver

class BaiduUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.baidu.com/")

    def test1_search(self):
        driver = self.driver
        # driver.open()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        products = driver.find_elements_by_xpath('//h3[@class="t"]/a')
        for product in products:
            print(product.text)
        print("product.len = " + str(products.__len__()))
        self.assertEqual(5, len(products), msg="不相等")

    def test2_search_name(self):
        driver = self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        products = driver.find_elements_by_xpath('//h3[@class="t"]/a')
        for product in products:
            print(product.text)
        print("product.len = " + str(products.__len__()))
        self.assertEqual(7, len(products), msg="不相等")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
