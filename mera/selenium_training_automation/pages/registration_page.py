"""
Created on Sep 14, 2015

@author: Mikhail
"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

# Project's imports
from mera.selenium_training_automation.pages.page import Page

__author__ = 'Mikhail'


class RegistrationPage(Page):

    def __init__(self, driver, url):
        Page.__init__(self, driver, url)
        self.url = "https://edit.yahoo.com/registration"
        self.main_container_xpath = "//div[@class='main']"
        self.input_container_xpath = "//form[@id='info-form']/div[@class='input-container']"
        self.name_validation_message_id = "name-validation-message"
        self.username_validation_message_id = "user-name-validation-message"
        self.password_validation_message_id = "password-validation-message"
        self.mobile_validation_message_id = "mobile-validation-message"
        self.day_of_birth_validation_message_id = "dob-validation-message"
        self.gender_validation_message_id = "gender-validation-message"
        self.validation_message_xpath = self.input_container_xpath + "//p[contains(@class, 'validation-message')]"

    @property
    def main_container(self):
        return self.driver.find_element_by_xpath(self.main_container_xpath)

    @property
    def input_container(self):
        return self.main_container.find_element_by_xpath(self.input_container_xpath)

    @property
    def header(self):
        return self.main_container.find_element_by_tag_name('h1')

    @property
    def first_name(self):
        return self.input_container.find_element_by_id('first-name')

    @property
    def second_name(self):
        return self.input_container.find_element_by_id('last-name')

    @property
    def user_name(self):
        return self.input_container.find_element_by_id('user-name')

    @property
    def password(self):
        return self.input_container.find_element_by_id('password')

    # Mobile phone

    @property
    def mobile(self):
        return self.input_container.find_element_by_id('mobile')

    def select_country_code(self, country_code):
        self.input_container.find_element_by_css_selector('.country-code-arrow').click()
        country_code_containers = self.input_container.find_element_by_id('country-codes-menu-1')
        country_code_element = country_code_containers.find_element_by_xpath(".//a[@data-code='{}']".format(country_code))
        webdriver.ActionChains(self.driver).move_to_element(country_code_element).click().perform()

    # Birthday

    @property
    def month(self):
        return Select(self.input_container.find_element_by_id('month'))

    @property
    def day(self):
        return Select(self.input_container.find_element_by_id('day'))

    @property
    def year(self):
        return Select(self.input_container.find_element_by_id('year'))

    # Sex

    @property
    def male(self):
        return self.input_container.find_element_by_id('male')

    @property
    def female(self):
        return self.input_container.find_element_by_id('female')

    @property
    def submit_button(self):
        return self.input_container.find_element_by_css_selector('.button.submit.btn-purple')

    # Validation messages
    # User first and last name
    @property
    def name_validation_message(self):
        return self.input_container.find_element_by_id(self.name_validation_message_id)

    @property
    def is_name_validation_message_visible(self):
        return self.is_element_visible_by_locator((By.ID, self.name_validation_message_id))

    # Username or email
    @property
    def username_validation_message(self):
        return self.input_container.find_element_by_id(self.username_validation_message_id)

    @property
    def is_username_validation_message_visible(self):
        return self.is_element_visible_by_locator((By.ID, self.username_validation_message_id))

    # Password
    @property
    def password_validation_message(self):
        return self.input_container.find_element_by_id(self.password_validation_message_id)

    @property
    def is_password_validation_message_visible(self):
        return self.is_element_visible_by_locator((By.ID, self.password_validation_message_id))

    # Mobile
    @property
    def mobile_validation_message(self):
        return self.input_container.find_element_by_id(self.mobile_validation_message_id)

    @property
    def is_mobile_validation_message_visible(self):
        return self.is_element_visible_by_locator((By.ID, self.mobile_validation_message_id))

    # Day of birth
    @property
    def day_of_birth_validation_message(self):
        return self.input_container.find_element_by_id(self.day_of_birth_validation_message_id)

    @property
    def is_day_of_birth_validation_message_visible(self):
        return self.is_element_visible_by_locator((By.ID, self.day_of_birth_validation_message_id))

    # Gender
    @property
    def gender_validation_message(self):
        return self.input_container.find_element_by_id(self.gender_validation_message_id)

    @property
    def is_gender_validation_message_visible(self):
        return self.is_element_visible_by_locator((By.ID, self.gender_validation_message_id))

    # Validation message box
    @property
    def validation_message_boxes(self):
        return self.input_container.find_elements_by_xpath(self.validation_message_xpath)

    @property
    def is_validation_message_box_visible(self):
        for validation_message_box in self.validation_message_boxes:
            if self.is_element_visible(validation_message_box):
                return True
        return False
