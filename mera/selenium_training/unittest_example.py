# coding=UTF-8
'''
Created on Aug 30, 2015

@author: Mikhail
'''

import unittest
from mera.selenium_training.home_page_functionality import HomePage

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"

class UnitTestExample(unittest.TestCase):
    
    page = HomePage()

    # This method will be called before execution of tests from the class
    @classmethod
    def setUpClass(cls):
        print "Unittest set-up class method"
        cls.page.start_browser()
    
    # This method will be called before execution of each test
    def setUp(self):
        print "Unittest set-up method"
        if self.page.number_of_opened_windows() == 0:
            print "Start new browser instance"
            self.page.start_browser()
        
    def testCorrectCheckTitle(self):
        actual_title = self.page.open_web_page(yandex_url)
        self.assertEqual(yandex_title, actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(yandex_title, actual_title))
        
    def testIncorrectCheckTitle(self):
        actual_title = self.page.open_web_page(google_url)
        self.assertEqual(yandex_title, actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(yandex_title, actual_title))

    # This method will be called after execution of each test
    def tearDown(self):
        print "Unittest tear-down method"
        self.page.close_browser_window()

    # This method will be called after execution of tests from the class
    @classmethod
    def tearDownClass(cls):
        print "Unittest tear-down class method"
        cls.page.stop_browser()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)