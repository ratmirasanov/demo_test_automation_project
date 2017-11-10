"""Module LoginPage for mapping the login page of Youtube."""

import time

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page_objects import PageObject, PageElement
import config
from utilities import Utilities


class LoginPage(PageObject, Utilities):
    """Class LoginPage for mapping the login page of Youtube."""

    email_field = PageElement(id_="identifierId")
    next_email_button = PageElement(id_="identifierNext")
    password_field = PageElement(css=".whsOnd.zHQkBf")
    next_password_button = PageElement(id_="passwordNext")

    def login(self, email=config.USER1['email'], password=config.USER1['password']):
        """A method for login on the Youtube."""

        self.email_field = email
        self.next_email_button.click()
        time.sleep(config.DELAY2)
        self.wait_visibility_by_css(".whsOnd.zHQkBf")
        self.password_field = password
        self.next_password_button.click()
        self.wait_visibility_by_css("#avatar-btn")

    def wait_visibility_by_css(self, css_path, timeout=config.DELAY1):
        """The overridden method from Utilities class."""

        return ui.WebDriverWait(self.w, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_path)))
