"""
Created on Aug 30, 2015

@author: Mikhail
"""
import nose

from mera.selenium_training.home_page_functionality import HomePage
from nose.tools import with_setup
from nose.tools import eq_

__author__ = 'Mikhail'

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


page = HomePage()
url = None


# This method will be called before execution of all tests
def setup_module():
    print "NoseTests set-up module method for generators"
    page.start_browser()


# This method will be called before execution of special tests
def setup_any():
    global page
    print "NoseTests set-up method for generators"
    if page.number_of_opened_windows() == 0:
        print "Start new browser instance"
        page.start_browser()


# This method will be called after execution of each test
def teardown_any():
    global page
    print "NoseTests tear-down method for generators"
    page.close_browser_window()


# This method will be called after execution of tests from the class
def teardown_module():
    global page
    print "NoseTests tear-down module method for generators"
    page.stop_browser()


@with_setup(setup=setup_any, teardown=teardown_any)
def testCheckTitleFunction():
    for test_url, test_title in [[t_url, t_title]
                                 for t_url in [yandex_url, google_url]
                                 for t_title in [yandex_title, google_title]]:
        yield check_title, test_url, test_title


# Function that will be used in generator
def check_title(url, expected_title):
    global page
    actual_title = page.open_web_page(url)
    eq_(expected_title,
        actual_title,
        "Title is incorrect. Expected '{}', Actual '{}'".format(expected_title, actual_title))


# Class that will be used in generator (as callable object)
class CheckTitle():
    def __call__(self, url, expected_title):
        self.description = "Checking url: '{}' with title '{}'".format(url, expected_title)
        actual_title = page.open_web_page(url)
        eq_(expected_title,
            actual_title,
            "Title is incorrect. Expected '{}', Actual '{}'".format(expected_title, actual_title))


@with_setup(setup=setup_any, teardown=teardown_any)
def testCheckTitleClass():
    for test_url, test_title in [[t_url, t_title]
                                 for t_url in [yandex_url, google_url]
                                 for t_title in [yandex_title, google_title]]:
        yield CheckTitle(), test_url, test_title

if __name__ == "__main__":
    nose.runmodule()
