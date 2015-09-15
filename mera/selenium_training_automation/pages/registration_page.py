"""
Created on Sep 14, 2015

@author: Mikhail
"""
from page import Page
from selenium.webdriver.support.select import Select
from selenium import webdriver

__author__ = 'Mikhail'


class RegistrationPage(Page):

    @property
    def first_name(self):
        return self.driver.find_element_by_id('first-name')

    @property
    def second_name(self):
        return self.driver.find_element_by_id('last-name')

    def select_country_code(self, country_code):
        self.driver.find_element_by_css_selector('.country-code-arrow').click()
        country_code_containers = self.driver.find_element_by_id('country-codes-menu-1')
        country_code_element = country_code_containers.find_element_by_xpath(".//a[@data-code='{}']".format(country_code))
        webdriver.ActionChains(self.driver).move_to_element(country_code_element).click().perform()

    @property
    def month(self):
        return Select(self.driver.find_element_by_id('month'))

