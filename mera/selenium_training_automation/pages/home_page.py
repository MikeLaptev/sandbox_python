"""
Created on Sep 14, 2015

@author: Mikhail
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from page import Page

__author__ = 'Mikhail'


class HomePage(Page):

    def open_home_page(self):
        self.open_page(self.url)

    @property
    def sign_in_field(self):
        return self.driver.find_element_by_css_selector(".tab-label.fz-xs.accent.sign-in")

    def go_to_registration_page(self):
        # put mouse cursor on it
        webdriver.ActionChains(self.driver).move_to_element(self.sign_in_field).perform()
        # wait until pop-up appear
        sign_up_element = self.wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".y-hdr-link.sign-up")))
        sign_up_element.click()
