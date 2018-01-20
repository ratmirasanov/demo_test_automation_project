"""Module MainPage for mapping the main page of Youtube."""

from page_objects import PageObject, PageElement


class MainPage(PageObject):
    """Class MainPage for mapping the main page of Youtube."""

    # Mapping web elements on the page.
    login_button = PageElement(css="#button>#text.style-scope.ytd-button-renderer.style-brand")

    def goto_login_page(self):
        """A method for opening the login page on the Youtube."""

        self.login_button.click()
