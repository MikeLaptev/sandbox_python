"""
Created on Sep 14, 2015

@author: Mikhail
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *

# Project's imports
from mera.selenium_training_automation.pages.page import Page

__author__ = 'Mikhail'


class HomePage(Page):

    def __init__(self, driver, url):
        Page.__init__(self, driver, url)
        self.url = "http://www.yahoo.com"
        self.sign_in_css_selector = ".tab-label.fz-xs.accent.sign-in"
        self.sign_in_xpath = "//a[@class='tab-label fz-xs accent sign-in ']"
        self.sign_up_css_selector = ".y-hdr-link.sign-up"

    def open_home_page(self):
        self.open_page(self.url)

    @property
    def sign_in_field(self):
        # return self.driver.find_element_by_css_selector(self.sign_in_css_selector)
        return self.driver.find_element_by_xpath(self.sign_in_xpath)

    def go_to_registration_page(self):
        # put mouse cursor on it
        webdriver.ActionChains(self.driver).move_to_element(self.sign_in_field).perform()
        # wait until pop-up appear
        sign_up_element = self.wait.until(visibility_of_element_located((By.CSS_SELECTOR, self.sign_up_css_selector)))
        sign_up_element.click()
