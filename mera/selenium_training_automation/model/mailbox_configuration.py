"""
Created on Sep 14, 2015

@author: Mikhail
"""

__author__ = "Mikhail"


class NewMailBoxSettings(object):

    def __init__(
        self,
        firstname="Mike",
        secondname="Laptev",
        password="OneTwoThree",
        email_id="mikhail.laptev",
        mobile_number="1234567890",
        country_code_value="1",
        day="9",
        month="September",
        year="1999",
        male=True,
    ):
        self.user_firstname = firstname
        self.user_secondname = secondname
        self.user_password = password
        self.user_email_id = email_id
        self.user_phone_number = mobile_number
        self.user_country_code = country_code_value
        self.user_birth_day = day
        self.user_birth_month = month
        self.user_birth_year = year
        self.is_user_male = male

    def get_full_name(self):
        return ", ".join([self.user_secondname, self.user_firstname])

    def get_full_name_with_email_id(self):
        return "{} [{}]".format(self.get_full_name(), self.user_email_id)
