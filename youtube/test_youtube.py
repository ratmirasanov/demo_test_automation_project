"""Module YoutubeTest for testing different features of Youtube."""

import unittest
import time

import config
from utilities import Utilities


class YoutubeTest(unittest.TestCase, Utilities):
    """Class YoutubeTest for testing different features of Youtube."""
    # Set URL.
    URL = ""

    def setUp(self):
        self._set_up()

    def test_login_to_youtube(self):
        """A method for login on the Youtube."""

        # Finding elements on the page and actions.
        login_button_element = self.find_by_css\
            ("#button>#text.style-scope.ytd-button-renderer.style-brand")
        self.click(login_button_element)

        email_field_element = self.find_by_id("identifierId")
        email_field_element.send_keys(config.USER1['email'])
        next_email_button_element = self.find_by_id("identifierNext")
        self.click(next_email_button_element)
        time.sleep(config.DELAY2)

        # Waiting for field to appear.
        self.wait_visibility_by_css(".whsOnd.zHQkBf")

        # Finding elements on the page and actions.
        password_field_element = self.find_by_css(".whsOnd.zHQkBf")
        password_field_element.send_keys(config.USER1['password'])
        next_password_button_element = self.find_by_id("passwordNext")
        self.click(next_password_button_element)

        # Waiting for button to appear.
        self.wait_visibility_by_css("#avatar-btn")

        self.make_screenshot()

        print('Test 1: User is successfully logged in.')

    def tearDown(self):
        self._tear_down()


if __name__ == '__main__':
    unittest.main()
