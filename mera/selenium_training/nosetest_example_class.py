"""
Created on Aug 30, 2015

@author: Mikhail
"""

import nose

from .home_page_functionality import HomePage
from nose.tools import eq_

__author__ = "Mikhail"

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


# Name of the class should start with [Tt]est prefix
# to make sure that it will be launched from the this script.
class TestNoseTestExample:

    page = HomePage()

    # This method will be called before execution of tests from the class
    @classmethod
    def setup_class(cls):
        print("NoseTests set-up class method")
        cls.page.start_browser()

    # This method will be called before execution of each test
    def setUp(self):
        print("NoseTests set-up method")
        if self.page.number_of_opened_windows() == 0:
            print("Start new browser instance")
            self.page.start_browser()

    # This method will be called after execution of each test
    def tearDown(self):
        print("NoseTests tear-down method")
        self.page.close_browser_window()

    # This method will be called after execution of tests from the class
    @classmethod
    def teardown_class(cls):
        print("NoseTests tear-down class method")
        cls.page.stop_browser()

    def testCorrectCheckTitleYandex(self):
        expected_title = yandex_title
        actual_title = self.page.open_web_page(yandex_url)
        eq_(
            expected_title,
            actual_title,
            "Title is incorrect. Expected '{}', Actual '{}'".format(
                expected_title, actual_title
            ),
        )

    def testIncorrectCheckTitleYandex(self):
        expected_title = google_title
        actual_title = self.page.open_web_page(yandex_url)
        eq_(
            expected_title,
            actual_title,
            "Title is incorrect. Expected '{}', Actual '{}'".format(
                expected_title, actual_title
            ),
        )

    def testCorrectCheckTitleGoogle(self):
        expected_title = google_title
        actual_title = self.page.open_web_page(google_url)
        eq_(
            expected_title,
            actual_title,
            "Title is incorrect. Expected '{}', Actual '{}'".format(
                expected_title, actual_title
            ),
        )

    def testIncorrectCheckTitleGoogle(self):
        expected_title = yandex_title
        actual_title = self.page.open_web_page(google_url)
        eq_(
            expected_title,
            actual_title,
            "Title is incorrect. Expected '{}', Actual '{}'".format(
                expected_title, actual_title
            ),
        )


if __name__ == "__main__":
    nose.runmodule()
