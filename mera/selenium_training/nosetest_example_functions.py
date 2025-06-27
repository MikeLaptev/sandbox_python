"""
Created on Aug 30, 2015

@author: Mikhail
"""

import nose

from .home_page_functionality import HomePage
from nose.tools import with_setup
from nose.tools import eq_

__author__ = "Mikhail"

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


page = HomePage()
url = None


# This method will be called before execution of all tests
def setup_module():
    print("NoseTests set-up module method")
    page.start_browser()


# This method will be called before execution of special tests
def setup_yandex():
    global url, page
    print("NoseTests set-up method for Yandex")
    url = yandex_url
    if page.number_of_opened_windows() == 0:
        print("Start new browser instance")
        page.start_browser()


# This method will be called before execution of special tests
def setup_google():
    global url, page
    print("NoseTests set-up method for Google")
    url = google_url
    if page.number_of_opened_windows() == 0:
        print("Start new browser instance")
        page.start_browser()


# This method will be called after execution of each test
def teardown_any():
    global page
    print("NoseTests tear-down method")
    page.close_browser_window()


# This method will be called after execution of tests from the class
def teardown_module():
    global page
    print("NoseTests tear-down module method")
    page.stop_browser()


@with_setup(setup=setup_yandex, teardown=teardown_any)
def testCorrectCheckTitleYandex():
    global url, page
    expected_title = yandex_title
    actual_title = page.open_web_page(url)
    eq_(
        expected_title,
        actual_title,
        "Title is incorrect. Expected '{}', Actual '{}'".format(
            expected_title, actual_title
        ),
    )


@with_setup(setup=setup_yandex, teardown=teardown_any)
def testIncorrectCheckTitleYandex():
    global url, page
    expected_title = google_title
    actual_title = page.open_web_page(url)
    eq_(
        expected_title,
        actual_title,
        "Title is incorrect. Expected '{}', Actual '{}'".format(
            expected_title, actual_title
        ),
    )


@with_setup(setup=setup_google, teardown=teardown_any)
def testCorrectCheckTitleGoogle():
    global url, page
    expected_title = google_title
    actual_title = page.open_web_page(url)
    eq_(
        expected_title,
        actual_title,
        "Title is incorrect. Expected '{}', Actual '{}'".format(
            expected_title, actual_title
        ),
    )


@with_setup(setup=setup_google, teardown=teardown_any)
def testIncorrectCheckTitleGoogle():
    global url, page
    expected_title = yandex_title
    actual_title = page.open_web_page(url)
    eq_(
        expected_title,
        actual_title,
        "Title is incorrect. Expected '{}', Actual '{}'".format(
            expected_title, actual_title
        ),
    )


if __name__ == "__main__":
    nose.runmodule()
