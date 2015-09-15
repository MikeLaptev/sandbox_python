"""
Created on Aug 30, 2015

@author: Mikhail
"""

from selenium import webdriver
from time import sleep
import re

__author__ = 'Mikhail'


class HomePage:

    def __init__(self):
        self.page_url = None
        self.driver = None

    def start_browser(self, browser_type='Firefox'):
        if re.match("firefox", browser_type, re.I):
            self.driver = webdriver.Firefox()
        elif re.match("chrome", browser_type, re.I):
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def number_of_opened_windows(self):
        number = 0
        try:
            number = len(self.driver.window_handles)
        finally:
            return number

    def open_web_page(self, url):
        self.driver.get(url)
        return self.driver.title

    def close_browser_window(self):
        self.driver.close()
        # Additional sleep for 5 seconds to make sure 
        # that browser window has been closed properly.
        # If we remove that timeout, then call of function start_browser 
        # after close_browser_window may do nothing, since instance exists
        # but closing 
        sleep(3)

    def stop_browser(self):
        # we should check if any instance of driver exists in the system
        if self.number_of_opened_windows() != 0:
            self.driver.quit()
