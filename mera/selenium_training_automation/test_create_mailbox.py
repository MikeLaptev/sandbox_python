"""
Created on Sep 14, 2015

@author: Mikhail
"""
from webdriver_fixture import application
from .model.mailbox_configuration import NewMailBoxSettings
from time import sleep

__author__ = 'Mikhail'


def test_create_mailbox(application):
    # from home page
    home_page = application.home_page
    home_page.open_home_page()
    expected_title = 'Yahoo'
    assert application.get_title() == expected_title, \
        "Incorrect title. Step 1. Expected: {}. Actual {}".format(expected_title, application.get_title())
    # workflow switches to registration page
    home_page.go_to_registration_page()
    expected_title = 'Yahoo Registration'
    assert application.get_title() == expected_title, \
        "Incorrect title. Step 2. Expected: {}. Actual {}".format(expected_title, application.get_title())
    # fill values on registration page
    new_mailbox_settings = NewMailBoxSettings()
    registration_page = application.registration_page
    registration_page.first_name.send_keys(new_mailbox_settings.user_firstname)
    registration_page.second_name.send_keys(new_mailbox_settings.user_secondname)
    registration_page.month.select_by_visible_text(new_mailbox_settings.user_birth_month)
    registration_page.select_country_code(new_mailbox_settings.user_country_code)

    sleep(10)



