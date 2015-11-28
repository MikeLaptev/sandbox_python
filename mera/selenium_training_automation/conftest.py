"""
Created on Sep 14, 2015

@author: Mikhail
"""
import pytest

__author__ = 'Mikhail'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type of Web Browser")
    parser.addoption("--url", action="store", default="https://www.yahoo.com/", help="Home page URL")
    parser.addoption("--proxy", action="store", default="No", help="Proxy Settings")


@pytest.fixture(scope="module")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="module")
def yahoo_home_page_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def proxy_settings(request):
    return request.config.getoption("--proxy")
