"""
Created on Sep 17, 2015

@author: Mikhail
"""

# Project's imports
from mera.selenium_training_automation.pages.page import Page

__author__ = "mlaptev"


class VerificationPage(Page):

    def __init__(self, driver, url):
        Page.__init__(self, driver, url)
        self.url = "https://edit.yahoo.com/registration"

    @property
    def header(self):
        return self.driver.find_element_by_tag_name("h1")

    @property
    def mobile(self):
        return self.driver.find_element_by_id("mobile")

    @property
    def mobile_value(self):
        return self.mobile.get_attribute("value")

    @property
    def detailed_country_code(self):
        return self.driver.find_element_by_id("country-name")

    @property
    def country_code(self):
        return (
            self.driver.find_element_by_id("selected-country-code-1")
            .text.replace(self.detailed_country_code.text, "")
            .strip()
        )

    @property
    def submit_button(self):
        return self.driver.find_element_by_css_selector(".button.submit.btn-purple")
