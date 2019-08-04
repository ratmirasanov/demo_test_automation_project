"""Module YoutubeTest for testing different features of Youtube."""

import unittest

import config
from utilities import Utilities


class YoutubeTest(unittest.TestCase, Utilities):
    """Class YoutubeTest for testing different features of Youtube."""

    # Set URL.
    URL = ""

    def setUp(self):
        """"Set up" -- method which is running before each test."""

        self._set_up()

    def test_login_to_youtube(self):
        """A method for login on the Youtube."""

        # Finding elements on the page and actions.
        self.find_clickable_by_css("#buttons a > .style-scope.ytd-button-renderer"
                                   ".style-suggestive.size-small[role='button']").click()
        self.find_clickable_by_id("identifierId").send_keys(config.USER1["email"])
        self.find_clickable_by_id("identifierNext").click()
        self.wait_invisibility_by_id("identifierId")
        self.find_clickable_by_css(".whsOnd.zHQkBf").send_keys(config.USER1["password"])
        self.find_clickable_by_id("passwordNext").click()

        try:
            self.find_clickable_by_css(".ZFr60d.CeoRYc").click()

        except:

            pass

        # Waiting for button to appear.
        self.wait_visibility_by_css("#avatar-btn")
        self.make_screenshot()
        print("Test 1: User is successfully logged in.")

    def tearDown(self):
        """"Tear down" -- method which is running after each test."""

        self._tear_down()


if __name__ == "__main__":
    unittest.main()
