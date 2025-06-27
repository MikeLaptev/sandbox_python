"""
Created on Sep 14, 2015

@author: Mikhail
"""

import pytest
from selenium import webdriver
from .model.application import Application
from selenium.webdriver.common.proxy import *

__author__ = "Mikhail"


@pytest.fixture(scope="module")
def application(request, browser_type, home_page_url, proxy_settings):
    if browser_type == "chrome":
        driver = webdriver.Chrome()
    else:
        if proxy_settings != "No":
            myProxy = proxy_settings

            proxy = Proxy(
                {
                    "proxyType": ProxyType.MANUAL,
                    "httpProxy": myProxy,
                    "ftpProxy": myProxy,
                    "sslProxy": myProxy,
                    "noProxy": "",  # set this value as desired
                }
            )
            driver = webdriver.Firefox(proxy=proxy)
        else:
            driver = webdriver.Firefox()

    driver.maximize_window()
    driver.implicitly_wait(10)
    # our teardown method
    request.addfinalizer(driver.quit)
    return Application(driver, home_page_url)
