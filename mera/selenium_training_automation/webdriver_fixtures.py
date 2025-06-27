"""
Created on Sep 14, 2015

@author: Mikhail
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.proxy import *

# Project's imports
from mera.selenium_training_automation.model.application import Application

__author__ = "Mikhail"


@pytest.fixture(scope="module")
def application(request, browser_type, yahoo_home_page_url, proxy_settings):
    if browser_type == "chrome":
        driver = webdriver.Chrome()
    else:
        if proxy_settings != "No":
            my_proxy = proxy_settings

            proxy = Proxy(
                {
                    "proxyType": ProxyType.MANUAL,
                    "httpProxy": my_proxy,
                    "ftpProxy": my_proxy,
                    "sslProxy": my_proxy,
                    "noProxy": "",  # set this value as desired
                }
            )
            driver = webdriver.Firefox(proxy=proxy)
        else:
            driver = webdriver.Firefox()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    # our teardown method
    request.addfinalizer(driver.quit)
    return Application(driver, yahoo_home_page_url)
