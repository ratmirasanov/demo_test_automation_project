"""Module Utilities with different useful methods."""

import datetime

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import config


class Utilities:
    """Class Utilities with different useful methods."""
    URL = ""
    auto_login = True

    def fill_form(self, data, path=''):
        """A method for filling html form on the page."""

        for key, val in data.items():
            if isinstance(val) != dict:

                try:
                    element_name = key

                    try:
                        if path != '':
                            element_name = '{}__{}'.format(path, element_name)

                        element = self.find_by_id(element_name)
                    except TimeoutException:
                        if path != '':
                            element_name = '{}[{}]'.format(path, element_name)

                        element = self.find_by_name(element_name)

                    element_tag = element.tag_name

                    # If we catch div, this means we are working with radiobutton.
                    if element_tag == 'div':
                        if path != '':
                            element_name = '{}[{}]'.format(path, element_name.split('__')[1])
                        self.set_radio_element(element_name, val)

                    else:
                        element_type = element.get_attribute("type")

                        if element_tag == 'select':
                            self.set_select_element(element, val)
                        elif element_tag == 'input' and element_type == 'radio':
                            self.set_radio_element(element_name, val)
                        elif element_tag == 'input' and element_type == 'checkbox':
                            self.set_checkbox_element(element)
                        else:
                            self.set_input_element(element, val)
                except Exception as error:
                    print('Error happens on element: ', key, val)
                    raise error
            else:
                self.fill_form(val, key)

    def _auto_login(self, user_token):
        # Go to URL.
        self.driver.get(config.DOMAIN + "/account/login?token=" + user_token)
        self.wait_invisibility_by_css(".loader_overlay")

    def _set_up(self, user_token=''):
        # Creation of instance of the browser.
        desired = DesiredCapabilities.CHROME
        desired['loggingPrefs'] = {'browser':'ALL'}
        self.driver = webdriver.Chrome(desired_capabilities=desired)

        if self.auto_login is True:
            self._auto_login(user_token)

        # Go to URL.
        self.driver.get(config.DOMAIN + self.URL)

        # Disable animations.
        self.driver.execute_script(
            "var style=document.createElement('style');"
            "style.type='text/css';style.appendChild("
            "document.createTextNode('*{transition: none !important;"
            "transition-property: none !important; transform: none !important;"
            "animation: none !important;}'));"
            "document.getElementsByTagName('head')[0].appendChild(style);"
        )

        # Maximize window.
        self.driver.maximize_window()

    def _tear_down(self):
        # Close the instance of the browser.
        self.driver.quit()

    def set_radio_element(self, element_name, val):
        """A method for setting radio button element on the page."""

        radio_elements = self.find_by_name_many(element_name)

        for element in radio_elements:
            if element.get_attribute('value') == val:
                self.driver.execute_script(
                    "arguments[0].scrollIntoView(true);"
                    "arguments[0].click();", element
                )
                return True
        return False

    def set_select_element(self, element, val):
        """A method for selecting an option in the select element on the page."""

        element = ui.Select(element)
        return element.select_by_visible_text(val)

    def set_checkbox_element(self, element):
        """A method for setting checkbox element on the page."""

        if element.is_selected() != True:
            self.click(element)

    def set_input_element(self, element, val):
        """A method for typing text into input element on the page."""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(val)

    def wait_invisibility_by_css(self, name, timeout=config.DELAY1):
        """A method for the invisibility of element located by CSS selector on the page."""

        ui.WebDriverWait(self.driver, timeout)\
            .until(EC.invisibility_of_element_located((By.CSS_SELECTOR, name)))

    def wait_invisibility(self, element, timeout=config.DELAY1):
        """A method for the invisibility of element located on the page."""

        ui.WebDriverWait(self.driver, timeout)\
            .until(EC.invisibility_of_element_located(element))

    def find_by_id(self, id_of_element, timeout=config.DELAY2):
        """A method for a finding of the element located by id on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.ID, id_of_element)))

    def find_clickable_by_id(self, id_of_element, timeout=config.DELAY2):
        """A method for a finding of the element to be clickable by id on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.element_to_be_clickable((By.ID, id_of_element)))

    def find_visible_by_id(self, id_of_element, timeout=config.DELAY2):
        """A method for a finding of the element to be visible by id on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((By.ID, id_of_element)))

    def find_by_name(self, name, timeout=config.DELAY2):
        """A method for a finding of the element located by name on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.NAME, name)))

    def find_clickable_by_name(self, name, timeout=config.DELAY2):
        """A method for a finding of the element to be clickable by name on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.element_to_be_clickable((By.NAME, name)))

    def find_by_name_many(self, name, timeout=config.DELAY2):
        """A method for a finding of the elements located by name on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_all_elements_located((By.NAME, name)))

    def find_by_css(self, css_path, timeout=config.DELAY2):
        """A method for a finding of the element located by CSS selector on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, css_path)))

    def find_clickable_by_css(self, css_path, timeout=config.DELAY2):
        """A method for a finding of the element to be clickable by CSS selector on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_path)))

    def find_visible_by_css(self, css_path, timeout=config.DELAY2):
        """A method for a finding of the element to be visible by CSS selector on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_path)))

    def find_by_css_many(self, css_path, timeout=config.DELAY2):
        """A method for a finding of the elements located by CSS selector on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_path)))

    def find_by_link(self, link_text, timeout=config.DELAY2):
        """A method for a finding of the element located by link text on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))

    def find_by_xpath(self, xpath, timeout=config.DELAY2):
        """A method for a finding of the element located by XPath on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_by_xpath_many(self, xpath, timeout=config.DELAY2):
        """A method for a finding of the elements located by XPath on the page."""

        return ui.WebDriverWait(self.driver, timeout)\
            .until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def click(self, element):
        """A method for a clicking on the element on the page."""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def print_logs(self):
        """A method for a printing logs of the console of the browser in the terminal."""

        logs = self.driver.get_log('browser')
        for log in logs:
            print(str(log))

    def make_screenshot(self):
        """A method for making a screenshot of the screen."""

        self.driver.get_screenshot_as_file("./screenshots/" +
                                           str(datetime.datetime.now().time()) +
                                           ".png"
                                           )

    def get_current_url(self):
        """A method for getting the current URL of page."""

        return self.driver.current_url
