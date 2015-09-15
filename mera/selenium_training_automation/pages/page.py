"""
Created on Sep 14, 2015

@author: Mikhail
"""
from selenium.webdriver.support.ui import WebDriverWait

__author__ = 'Mikhail'


class Page(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)
