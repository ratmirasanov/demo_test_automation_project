"""Module Utilities with different useful methods."""

import datetime
import time
import pickle
import json
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import config


class Utilities:
    """Class Utilities with different useful methods."""

    URL = ""
    driver = None

    def _set_up(self):

        # Creation of instance of the browser.
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1,
        })
        desired = DesiredCapabilities.CHROME
        desired["loggingPrefs"] = {"browser": "ALL"}
        desired.update(options.to_capabilities())
        self.driver = webdriver.Chrome(desired_capabilities=desired)
        # Maximize window size.
        self.driver.set_window_size(config.WIDTH, config.HEIGHT)

        # Go to URL.
        if config.DOMAIN.startswith("http"):

            self.driver.get(config.DOMAIN + self.URL)

        else:

            raise Exception("Invalid domain name. Use 'http' or 'https' before domain name.!")

    def _tear_down(self):

        # Close the instance of the browser.
        self.driver.quit()

    def set_radio_element(self, element_name, val):
        """A method for setting radio button element on the page."""

        radio_elements = self.find_by_name_many(element_name)

        for element in radio_elements:

            if element.get_attribute("value") == val:

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

        if element.is_selected() is not True:

            self.click(element)

    def set_input_element(self, element, val):
        """A method for typing text into input element on the page."""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(val)

    def wait_new_window_to_be_opened(self, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.new_window_is_opened(self.driver.window_handles))

    def wait_title_to_be(self, expected_title, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.title_is(expected_title))

    def wait_staleness_of(self, element, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.staleness_of(element))

    def wait_text_is_present_in_element_by_id(self, id_attribute, text, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.ID, id_attribute), text))

    def wait_text_is_present_in_element_by_css(self, css_selector, text, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), text))

    def wait_presence_by_id(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.ID, id_attribute)))

    def wait_presence_by_css(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    def wait_presence_by_id_many(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.ID, id_attribute)))

    def wait_presence_by_css_many(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector)))

    def wait_visibility_by_id(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.ID, id_attribute)))

    def wait_visibility_by_css(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def wait_visibility_by_id_many(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located((By.ID, id_attribute)))

    def wait_visibility_by_css_many(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, css_selector)))

    def wait_invisibility_by_id(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.ID, id_attribute)))

    def wait_invisibility_by_css(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def wait_availability_of_frame_by_id(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, id_attribute)))

    def wait_availability_of_frame_by_css(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, css_selector)))

    def wait_clickable_by_id(self, id_attribute, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.ID, id_attribute)))

    def wait_clickable_by_css(self, css_selector, timeout=config.DELAY1):

        return ui.WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    def find_by_id(self, id_attribute):

        return self.driver.find_element_by_id(id_attribute)

    def find_by_id_many(self, id_attribute):

        return self.driver.find_elements_by_id(id_attribute)

    def find_by_name(self, name):

        return self.driver.find_element_by_name(name)

    def find_by_name_many(self, name):

        return self.driver.find_elements_by_name(name)

    def find_by_class_name(self, class_name):

        return self.driver.find_element_by_class_name(class_name)

    def find_by_class_name_many(self, class_name):

        return self.driver.find_elements_by_class_name(class_name)

    def find_by_tag_name(self, tag_name):

        return self.driver.find_element_by_tag_name(tag_name)

    def find_by_tag_name_many(self, tag_name):

        return self.driver.find_elements_by_tag_name(tag_name)

    def find_by_link(self, link_text):

        return self.driver.find_element_by_link_text(link_text)

    def find_by_link_many(self, link_text):

        return self.driver.find_elements_by_link_text(link_text)

    def find_by_css(self, css_selector):

        return self.driver.find_element_by_css_selector(css_selector)

    def find_by_css_many(self, css_selector):

        return self.driver.find_elements_by_css_selector(css_selector)

    def find_by_xpath(self, xpath):

        return self.driver.find_element_by_xpath(xpath)

    def find_by_xpath_many(self, xpath):

        return self.driver.find_elements_by_xpath(xpath)

    def click(self, element):
        """A method for a clicking on the element on the page."""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_via_js(self, element):
        """A method for a clicking on the element on the page using JS."""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def print_logs(self):
        """A method for a printing logs of the console of the browser in the terminal."""

        logs = self.driver.get_log("browser")

        for log in logs:

            print(str(log))

    def make_screenshot(self):
        """A method for making a screenshot of the screen."""

        self.driver.get_screenshot_as_file(config.ROOT_DIR +
                                           "/screenshots/" +
                                           str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")) +
                                           ".png")

    def save_cookie(self, name):
        """A method for saving cookies for domain."""

        with open(name + ".pkl", "wb") as filehandler:

            pickle.dump(self.driver.get_cookies(), filehandler)

    def load_cookie(self, name):
        """A method for loading cookies for domain."""

        with open(name + ".pkl", "rb") as cookiesfile:

            cookies = pickle.load(cookiesfile)

            for cookie in cookies:

                if isinstance(cookie.get("expiry"), float):

                    cookie["expiry"] = int(cookie["expiry"])

                self.driver.add_cookie(cookie)

    def get_current_url(self):
        """A method for getting the current URL of page."""

        return self.driver.current_url

    def scroll_down(self):
        """A method for scrolling the page."""

        # Get scroll height.
        last_height = self.driver.execute_script("return document.body.scrollHeight;")

        while True:

            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page.
            time.sleep(config.SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script("return document.body.scrollHeight;")

            if new_height == last_height:

                break

            last_height = new_height

    def scroll_to_element(self, element):
        """A method for scrolling to the element."""

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def refresh_page(self):
        """A method for refreshing the page."""

        self.driver.refresh()

    def set_local_storage(self, key, value):
        """A method for setting key in local storage."""

        self.driver.execute_script(
            "window.localStorage.setItem('{}',{});".format(key, json.dumps(value)))

    def show_error_traceback(self):
        """A method for showing error traceback."""

        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        return [line, text]
