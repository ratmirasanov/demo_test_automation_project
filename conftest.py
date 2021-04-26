"""Module Conftest for Pytest."""
import pytest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import config


@pytest.fixture
def setup(request):
    """Setup function (fixture) for using with Pytest."""

    config.DOMAIN = "https://google.com/"
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.notifications": 1,
        },
    )
    options.add_experimental_option("prefs", {"intl.accept_languages": "en-GB"})
    desired = DesiredCapabilities.CHROME
    desired["loggingPrefs"] = {"browser": "ALL"}
    desired.update(options.to_capabilities())
    driver = webdriver.Chrome(desired_capabilities=desired)
    # Maximize window size.
    driver.set_window_size(config.WIDTH, config.HEIGHT)
    request.cls.driver = driver

    # Go to URL.
    if config.DOMAIN.startswith("http"):

        driver.get(config.DOMAIN)

    else:

        raise Exception(
            "Invalid domain name. Use 'http' or 'https' before domain name!"
        )

    yield driver

    driver.quit()
