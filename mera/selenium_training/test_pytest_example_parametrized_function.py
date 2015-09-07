'''
Created on Aug 30, 2015

@author: Mikhail
'''
import pytest

from mera.selenium_training.home_page_functionality import HomePage

yandex_title = "Yandex"
yandex_url = "https://www.yandex.com/"
google_title = "Google"
google_url = "http://www.google.com"


page = HomePage()

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
@pytest.fixture(scope="function")
def setup_function(request):
    global page
    print "Py.test set-up method"
    if page.number_of_opened_windows() == 0:
        print "Start new browser instance"
        page.start_browser()
    # This method will be called after execution of each test
    def fin():
        global page
        print "Py.test tear-down method"
        page.close_browser_window()
    request.addfinalizer(fin)

@pytest.mark.parametrize("test_url,test_title", 
                         [(yandex_url, yandex_title),
                          (yandex_url, google_title),
                          (google_url, google_title),
                          pytest.mark.xfail((google_url, yandex_title))])
@pytest.mark.usefixtures("setup_module", "setup_function")
def test_CheckTitle(test_url,test_title):
    global page
    actual_title = page.open_web_page(test_url)
    assert test_title == actual_title, "Title is incorrect. Expected '{}', Actual '{}'".format(test_title, actual_title)
    
if __name__ == "__main__":
    pytest.main(args=['-v', '-s'])