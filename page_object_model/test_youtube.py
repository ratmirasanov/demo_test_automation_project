"""Module YoutubeTest for testing different features of Youtube."""

import unittest

import config
from utilities import Utilities
from page_object_model.main_page import MainPage
from page_object_model.login_page import LoginPage


class YoutubeTest(unittest.TestCase, Utilities):
    """Class YoutubeTest for testing different features of Youtube."""
    # Set URL.
    URL = ""

    def setUp(self):
        """"Set up"- method which is running before each test."""

        self._set_up()

    def test_login_to_youtube(self):
        """A method for login on the Youtube."""

        main_page = MainPage(self.driver, root_uri=config.DOMAIN)
        main_page.goto_login_page()
        login_page = LoginPage(self.driver)
        login_page.login(config.USER1['email'], config.USER1['password'])

        self.make_screenshot()

        print("Test 1: User is successfully logged in.")

    def tearDown(self):
        """"Tear down"- method which is running after each test."""

        self._tear_down()


if __name__ == '__main__':
    unittest.main()
