"""Module TestGoogleV2 for testing different features of Google."""

import pytest

from selenium.webdriver.common.keys import Keys

from utilities import Utilities


@pytest.mark.usefixtures("setup")
class TestGoogleV2(Utilities):
    """Class TestGoogleV2 for testing different features of Google."""

    @pytest.mark.parametrize(
        "search_text, site_link",
        [
            ("facebook", "facebook.com"),
            ("apple", "apple.com"),
        ],
    )
    def test_google_search_v2(self, search_text, site_link):
        """A method for searching something on Google."""

        self.wait_clickable_by_css("input[name='q']").send_keys(
            search_text + Keys.ENTER
        )

        assert (
            self.wait_visibility_by_css(".B1uW2d.ellip.PZPZlf > .ellip").text
            == site_link
        )
