"""
Created on Sep 14, 2015

@author: Mikhail
"""

import pytest
from time import sleep

# Project's imports
from mera.selenium_training_automation.model.mailbox_configuration import (
    NewMailBoxSettings,
)
from mera.selenium_training_automation.webdriver_fixtures import *

__author__ = "Mikhail"


def id_function(value):
    if isinstance(value, NewMailBoxSettings):
        return value.get_full_name()


@pytest.mark.parametrize(
    argnames="settings",
    argvalues=[
        NewMailBoxSettings(),
        # pytest.mark.xfail(NewMailBoxSettings(email_id="mike.l"))
    ],
    ids=id_function,
)
def test_create_mailbox(settings, application):

    # from home page
    application.home_page
    application.home_page.open_home_page()
    expected_title = "Yahoo"
    assert (
        application.get_title() == expected_title
    ), "Incorrect title. Step 1. Expected: {}. Actual {}".format(
        expected_title, application.get_title()
    )
    # workflow switches to registration page
    application.home_page.go_to_registration_page()
    sleep(1)

    # check title
    expected_title = "Yahoo Registration"
    assert (
        application.get_title() == expected_title
    ), "Incorrect title on the registration page. Step 2. Expected: {}. Actual {}".format(
        expected_title, application.get_title()
    )

    # check header
    expected_header = "Sign up"
    assert (
        application.registration_page.header.text == expected_header
    ), "Incorrect header on the registration page. Step 3. Expected: {}. Actual {}".format(
        expected_header, application.registration_page.header.text
    )

    # fill values on registration page
    application.registration_page.first_name.send_keys(settings.user_firstname)
    application.registration_page.second_name.send_keys(settings.user_secondname)
    application.registration_page.user_name.send_keys(settings.user_email_id)
    application.registration_page.password.send_keys(settings.user_password)
    # mobile
    application.registration_page.select_country_code(settings.user_country_code)
    application.registration_page.mobile.send_keys(settings.user_phone_number)
    # birthday
    application.registration_page.month.select_by_visible_text(
        settings.user_birth_month
    )
    application.registration_page.day.select_by_visible_text(settings.user_birth_day)
    application.registration_page.year.select_by_visible_text(settings.user_birth_year)
    # sex
    if settings.is_user_male:
        application.registration_page.male.click()
    else:
        application.registration_page.female.click()

    # pre-checking
    if application.registration_page.is_validation_message_box_visible:
        # check input information on correctness
        assert (
            not application.registration_page.is_name_validation_message_visible
        ), application.registration_page.name_validation_message.text
        assert (
            not application.registration_page.is_username_validation_message_visible
        ), application.registration_page.username_validation_message.text
        assert (
            not application.registration_page.is_password_validation_message_visible
        ), application.registration_page.password_validation_message.text
        assert (
            not application.registration_page.is_mobile_validation_message_visible
        ), application.registration_page.mobile_validation_message.text
        assert (
            not application.registration_page.is_day_of_birth_validation_message_visible
        ), application.registration_page.day_of_birth_validation_message.text
        assert (
            not application.registration_page.is_gender_validation_message_visible
        ), application.registration_page.gender_validation_message.text

    # submit
    application.registration_page.submit_button.click()

    # refresh information about pages
    application.update_pages()

    # post-checking
    if application.registration_page.is_validation_message_box_visible:
        # check input information on correctness
        assert (
            not application.registration_page.is_name_validation_message_visible
        ), application.registration_page.name_validation_message.text
        assert (
            not application.registration_page.is_username_validation_message_visible
        ), application.registration_page.username_validation_message.text
        assert (
            not application.registration_page.is_password_validation_message_visible
        ), application.registration_page.password_validation_message.text
        assert (
            not application.registration_page.is_mobile_validation_message_visible
        ), application.registration_page.mobile_validation_message.text
        assert (
            not application.registration_page.is_day_of_birth_validation_message_visible
        ), application.registration_page.day_of_birth_validation_message.text
        assert (
            not application.registration_page.is_gender_validation_message_visible
        ), application.registration_page.gender_validation_message.text

    # workflow switches to verification page
    # check title
    expected_title = "Yahoo Registration"
    assert (
        application.get_title() == expected_title
    ), "Incorrect title on the verification page. Step 4. Expected: {}. Actual {}".format(
        expected_title, application.get_title()
    )

    # check header
    expected_header = "Verification"
    assert (
        application.verification_page.header.text == expected_header
    ), "Incorrect header on the verification page. Step 5. Expected: {}. Actual {}".format(
        expected_header, application.verification_page.header.text
    )

    # check mobile
    assert (
        application.verification_page.mobile_value == settings.user_phone_number
    ), "Incorrect mobile has been displayed on the verification page. Step 6. Expected: {}. Actual {}".format(
        settings.user_phone_number, application.verification_page.mobile_value
    )

    # check country-code
    assert (
        application.verification_page.country_code == "+" + settings.user_country_code
    ), "Incorrect mobile has been displayed on the verification page. Step 6. Expected: +{}. Actual {}".format(
        settings.user_country_code, application.verification_page.country_code
    )
