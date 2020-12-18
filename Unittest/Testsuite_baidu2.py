import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BaiduUnittest2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.baidu.com/")

    def test_serch_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "wd"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "kw"))

    # def test1_search(self):
    #     driver = self.driver
    #     # driver.open()
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("selenium")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(3)
    #     products = driver.find_elements_by_xpath('//h3[@class="t"]/a')
    #     for product in products:
    #         print(product.text)
    #     print("product.len = " + str(products.__len__()))
    #     self.assertEqual(5, len(products), msg="不相等")

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

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :param how:  By locator type
        :param what:  locator value
        :return:
        """
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True



if __name__ == "__main__":
    unittest.main(verbosity=2)
