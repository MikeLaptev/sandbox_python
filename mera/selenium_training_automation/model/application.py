"""
Created on Sep 14, 2015

@author: Mikhail
"""

# Project's imports
from mera.selenium_training_automation.pages.home_page import HomePage
from mera.selenium_training_automation.pages.registration_page import RegistrationPage
from mera.selenium_training_automation.pages.verification_page import VerificationPage

__author__ = "Mikhail"


class Application(object):

    def __init__(self, initializing_driver, home_page_url):
        self.driver = initializing_driver
        self.home_page_url = home_page_url
        self.home_page = HomePage(self.driver, self.home_page_url)
        # At the moment, url for the registration page will have the same value like for home page.
        self.registration_page = RegistrationPage(self.driver, self.home_page_url)
        self.verification_page = VerificationPage(self.driver, self.home_page_url)

    def update_pages(self):
        self.home_page = HomePage(self.driver, self.home_page_url)
        # At the moment, url for the registration page will have the same value like for home page.
        self.registration_page = RegistrationPage(self.driver, self.home_page_url)
        self.verification_page = VerificationPage(self.driver, self.home_page_url)

    def get_title(self):
        return self.driver.title
