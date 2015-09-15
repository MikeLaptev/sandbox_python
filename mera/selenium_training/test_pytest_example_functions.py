"""
Created on Aug 30, 2015

@author: Mikhail
"""
import pytest

from .home_page_functionality import HomePage

__author__ = 'Mikhail'

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


page = HomePage()
url = None


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


# This method will be called before execution of special tests
@pytest.fixture
def setup_yandex(request):
    global url, page
    print "Py.test set-up method for Yandex"
    url = yandex_url
    if page.number_of_opened_windows() == 0:
        print "Start new browser instance"
        page.start_browser()

    # This method will be called after execution of the test
    def fin():
        global page
        print "Py.test tear-down method"
        page.close_browser_window()
    request.addfinalizer(fin)


# This method will be called before execution of special tests
@pytest.fixture
def setup_google(request):
    global url, page
    print "Py.test set-up method for Google"
    url = google_url
    if page.number_of_opened_windows() == 0:
        print "Start new browser instance"
        page.start_browser()

    # This method will be called after execution of the test
    def fin():
        global page
        print "Py.test tear-down method"
        page.close_browser_window()
    request.addfinalizer(fin)


def test_CorrectCheckTitleYandex(setup_yandex):
    global url, page
    expected_title = yandex_title
    actual_title = page.open_web_page(url)
    assert expected_title == actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(expected_title,
                                                                                                   actual_title)


def test_IncorrectCheckTitleYandex(setup_yandex):
    global url, page
    expected_title = google_title
    actual_title = page.open_web_page(url)
    assert expected_title == actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(expected_title,
                                                                                                   actual_title)


def test_CorrectCheckTitleGoogle(setup_google):
    global url, page
    expected_title = google_title
    actual_title = page.open_web_page(url)
    assert expected_title, actual_title


def test_IncorrectCheckTitleGoogle(setup_google):
    global url, page
    expected_title = yandex_title
    actual_title = page.open_web_page(url)
    assert expected_title == actual_title


if __name__ == "__main__":
    pytest.main(args=['-v', '-s'])
