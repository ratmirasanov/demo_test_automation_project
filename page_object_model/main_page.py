"""Module MainPage for mapping the main page of Youtube."""

from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from page_objects import PageObject, PageElement
import config
from utilities import Utilities


class MainPage(PageObject, Utilities):
    """Class MainPage for mapping the main page of Youtube."""

    # Mapping web elements on the page.
    login_button = PageElement(css="#buttons a > .style-scope.ytd-button-renderer"
                                   ".style-suggestive.size-small[role='button']")

    def goto_login_page(self):
        """A method for opening the login page on the Youtube."""

        self.find_clickable_by_css("#buttons a > .style-scope.ytd-button-renderer"
                                   ".style-suggestive.size-small[role='button']")
        self.login_button.click()

    def find_clickable_by_css(self, css_selector, timeout=config.DELAY1):
        """The overridden method for waiting for clickability of web element on the page
         from Utilities class."""

        return ui.WebDriverWait(self.w, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
