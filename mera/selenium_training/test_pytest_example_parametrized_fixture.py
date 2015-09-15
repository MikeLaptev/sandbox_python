"""
Created on Aug 30, 2015

@author: Mikhail
"""
import pytest

from mera.selenium_training.home_page_functionality import HomePage

__author__ = 'Mikhail'

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


page = HomePage()
url = None
title = None


# This method will be called before execution of all tests
@pytest.fixture(scope="module")
def setup_module(request):
    print "Py.test set-up module method"
    page.start_browser()

    # This method will be called after execution of all tests
    def fin():
        global page
        print "Py.test tear-down module method"
        page.stop_browser()
    request.addfinalizer(fin)


# This function returns id for fixture value
def id_fixture_function(fixture_value):
    """
    # First variant of implementation
    if fixture_value[0] == yandex_url:
        return " Yandex"
    elif fixture_value[1] == google_url:
        return " Google"
    else:
        return None
    """
    # second variant of implementation
    return "Url: '{}'. Title: '{}'".format(*fixture_value)


# This method will be called before execution of special tests
@pytest.fixture(scope="function",
                params=[[t_url, t_title]
                          for t_url in [yandex_url, google_url]
                          for t_title in [yandex_title, google_title]],
                ids=id_fixture_function)
def setup(request):
    global url, title, page
    print "Py.test set-up method"
    url = request.param[0]
    title = request.param[1]
    if page.number_of_opened_windows() == 0:
        print "Start new browser instance"
        page.start_browser()

    # This method will be called after execution of each test
    def fin():
        global page
        print "Py.test tear-down method"
        page.close_browser_window()
    request.addfinalizer(fin)


def test_CheckTitle(setup):
    global url, title, page
    actual_title = page.open_web_page(url)
    assert title == actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(title, actual_title)

if __name__ == "__main__":
    pytest.main(args=['-v', '-s'])
