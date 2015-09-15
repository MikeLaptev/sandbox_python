"""
Created on Sep 14, 2015

@author: Mikhail
"""

__author__ = 'Mikhail'


class NewMailBoxSettings(object):

    def __init__(self,
                 firstname="Mikhail",
                 secondname="Laptev",
                 password="OneTwoThree",
                 email_id="mikhail.laptev",
                 mobile_number="9853442213",
                 country_code_value="7",
                 day="04",
                 month="June",
                 year="1985"):
        self.user_firstname = firstname
        self.user_secondname = secondname
        self.user_password = password
        self.user_email_id = email_id
        self.user_phone_number = mobile_number
        self.user_country_code = country_code_value
        self.user_birth_day = day
        self.user_birth_month = month
        self.user_birth_year = year
