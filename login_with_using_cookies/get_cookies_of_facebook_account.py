"""Module for saving cookies for the domain."""

import time

import config
from utilities import Utilities


class GetCookies(Utilities):
    """Class for saving cookies for the domain."""

    def __init__(self, email="", password=""):
        """Method for saving cookies for the domain."""

        config.DOMAIN = "https://facebook.com"
        self._set_up()
        # Go to URL.
        self.driver.get(config.DOMAIN)
        # Finding elements on the page and actions.
        self.wait_visibility_by_id("email").send_keys(email)
        self.find_by_id("pass").send_keys(password)
        self.find_by_id("loginbutton").click()
        # Saving user's cookies.
        self.save_cookie("ratmir.asanov.demo")
        time.sleep(config.DELAY2)
        self._tear_down()


if __name__ == "__main__":
    COOKIE = GetCookies(config.USER1["email"], config.USER1["password"])
