'''
Created on Aug 30, 2015

@author: Mikhail
'''
import pytest
import re

from mera.selenium_training.home_page_functionality import HomePage

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


page = HomePage()
url = None
title = None
current_browser = None

def id_fixture_module(fixture_value):
    # First variant of implementation
    if re.match("chrome", fixture_value, re.I):
        return " Google Chrome. "
    elif re.match("firefox", fixture_value, re.I):
        return " Mozilla FireFox. "
    else:
        return None

# This method will be called before execution of all tests
@pytest.fixture(scope="module",
                params = ['Chrome', 'Firefox'],
                ids = id_fixture_module)
def setup_module(request):
    global current_browser
    print "Py.test set-up module method"
    page.start_browser(request.param)
    current_browser = request.param
    # This method will be called after execution of all tests
    def fin():
        global page
        print "Py.test tear-down module method"
        page.stop_browser()
    request.addfinalizer(fin)

# This method will be called before tests execution
@pytest.fixture(scope="function")
def setup(request):
    global page, current_browser
    print "Py.test set-up method"
    if page.number_of_opened_windows() == 0:
        print "Start new browser instance"
        page.start_browser(current_browser if current_browser is not None else 'Firefox')
    # This method will be called after execution of each test
    def fin():
        global page
        print "Py.test tear-down method"
        page.close_browser_window()
    request.addfinalizer(fin)
    
# This function returns id for fixture value (url)
def id_fixture_function_url_value(fixture_value):
    return " Url: '{}'. ".format(fixture_value)


@pytest.fixture(scope="function",
                params = [yandex_url, google_url],
                ids = id_fixture_function_url_value)
def setup_function_url(request):
    global url
    print "Py.test set-up method for url"
    url = request.param
    
# This function returns id for fixture value (title)
def id_fixture_function_title_value(fixture_value):
    return " Title: '{}'. ".format(fixture_value)


@pytest.fixture(scope="function",
                params = [yandex_title, google_title],
                ids = id_fixture_function_title_value)
def setup_function_title(request):
    global title, page
    print "Py.test set-up method for title"
    title = request.param

def test_CheckTitle(setup_module, setup, setup_function_url, setup_function_title):
    global url, title, page
    actual_title = page.open_web_page(url)
    assert title == actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(title, actual_title)
    
if __name__ == "__main__":
    pytest.main(args=['-v', '-s'])