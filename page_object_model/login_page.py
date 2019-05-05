"""Module LoginPage for mapping the login page of Youtube."""

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page_objects import PageObject, PageElement
import config
from utilities import Utilities


class LoginPage(PageObject, Utilities):
    """Class LoginPage for mapping the login page of Youtube."""

    # Mapping web elements on the page.
    email_field = PageElement(id_="identifierId")
    next_email_button = PageElement(id_="identifierNext")
    password_field = PageElement(css=".whsOnd.zHQkBf")
    next_password_button = PageElement(id_="passwordNext")

    def login(self, email=config.USER1["email"], password=config.USER1["password"]):
        """A method for login on the Youtube."""

        self.find_clickable_by_id("identifierId")
        self.email_field = email
        self.find_clickable_by_id("identifierNext")
        self.next_email_button.click()
        self.wait_invisibility_by_id("identifierNext")
        self.find_clickable_by_css(".whsOnd.zHQkBf")
        self.password_field = password
        self.find_clickable_by_id("passwordNext")
        self.next_password_button.click()
        self.wait_visibility_by_css("#avatar-btn")

    def wait_visibility_by_css(self, css_selector, timeout=config.DELAY1):
        """The overridden method for waiting for visibility of web element on the page
         from Utilities class."""

        return ui.WebDriverWait(self.w, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def wait_invisibility_by_id(self, id_attribute, timeout=config.DELAY1):
        """The overridden method for waiting for invisibility of web element on the page
         from Utilities class."""

        return ui.WebDriverWait(self.w, timeout).until(
            EC.invisibility_of_element_located((By.ID, id_attribute)))

    def find_clickable_by_id(self, id_attribute, timeout=config.DELAY1):
        """The overridden method for waiting for clickability of web element on the page
                 from Utilities class."""

        return ui.WebDriverWait(self.w, timeout).until(
            EC.element_to_be_clickable((By.ID, id_attribute)))

    def find_clickable_by_css(self, css_selector, timeout=config.DELAY1):
        """The overridden method for waiting for clickability of web element on the page
         from Utilities class."""

        return ui.WebDriverWait(self.w, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
