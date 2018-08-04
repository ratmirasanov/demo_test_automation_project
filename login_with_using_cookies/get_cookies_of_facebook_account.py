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
        email_text_field_element = self.wait_visibility_by_id("email")
        email_text_field_element.clear()
        email_text_field_element.send_keys(email)

        password_text_field_element = self.find_by_id("pass")
        password_text_field_element.clear()
        password_text_field_element.send_keys(password)

        login_button = self.find_by_id("loginbutton")
        self.click(login_button)

        # Saving user's cookies.
        self.save_cookie("ratmir.asanov.demo")
        time.sleep(config.DELAY2)

        self._tear_down()


if __name__ == '__main__':
    COOKIE = GetCookies(config.USER1['email'], config.USER1['password'])
