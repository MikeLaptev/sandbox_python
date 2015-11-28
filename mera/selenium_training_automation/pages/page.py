"""
Created on Sep 14, 2015

@author: Mikhail
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, visibility_of
from selenium.common.exceptions import TimeoutException

__author__ = 'Mikhail'


class Page(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 5)

    def open_page(self, url):
        self.driver.get(url)

    def is_element_visible_by_locator(self, locator):
        try:
            self.wait.until(visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_visible(self, element):
        try:
            self.wait.until(visibility_of(element))
        except TimeoutException:
            return False
        return True
