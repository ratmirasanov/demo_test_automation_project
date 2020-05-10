"""Module TestGoogleV1 for testing different features of Google."""

import pytest

from selenium.webdriver.common.keys import Keys

import config
from utilities import Utilities


class TestGoogleV1(Utilities):
    """Class TestGoogleV1 for testing different features of Google."""

    # Set URL.
    URL = ""

    def setup_method(self):
        """"Set up" -- method which is running before each test."""

        config.DOMAIN = "https://google.com/"
        self._set_up()

    @pytest.mark.parametrize("search_text, site_link", [
        ("facebook", "facebook.com"),
        ("apple", "apple.com"),
    ])
    def test_google_search_v1(self, search_text, site_link):
        """A method for searching something on Google."""

        self.wait_clickable_by_css("input[name='q']").send_keys(search_text + Keys.ENTER)

        assert self.wait_visibility_by_css(".B1uW2d.ellip.PZPZlf > .ellip").text == site_link

    def teardown_method(self):
        """"Tear down" -- method which is running after each test."""

        self._tear_down()
