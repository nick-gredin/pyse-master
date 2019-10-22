# from UtilityPackage.SeleniumDriver import SeleniumDriver
import logging
import re
import string
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from pyse import driver
from .pyse_api import WebDriver

"""
Services class : Page class which contains all the methods for interaction with elements
"""


class Services(WebDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators in registration page to github    #Locator types for reference
    _UserNameField = "user[login]"  # id

    def is_element_present(self, locator):
        """
        This method is to verify element is present or not.

        param locator: XPATH of given element
        param_type: string
        """
        try:
            element = self.driver.find_element_by_xpath(locator)
            logging.info("# Element '%s' is present." % locator)
            if element.is_displayed():
                return True
        except NoSuchElementException:
            logging.info("# Element '%s' is not present." % locator)
            return False

    def click_button(self, value, buttonType):
        """
        This method clicking on buttons.Please provide button type listed below
        """
        _TabButton = "//a[text()='" + value + "']"
        _Button = "//span[contains(text(), '" + value + "')]"
        _CloseWindowButton = "//span[contains(@title, '" + value + "')]"
        if buttonType == "tabButton":
            if Services.is_element_present(self, _TabButton) is True:
                element = WebDriver.get_element(self, _TabButton, "xpath")
                element.click()
                self.sleep(3)
        elif buttonType == "button":
            if self.is_element_present(_Button) is True:
                element = WebDriver.get_element(self, _Button, "xpath")
                element.click()
                self.sleep(4)
            else:
                _Button2 = "//button[@name='Submit']"
                element = self.driver.find_element_by_xpath(_Button2)
                element.click()
                self.sleep(4)
        elif buttonType == "closeWindowButton":
            if Services.is_element_present(self, _CloseWindowButton) is True:
                element = WebDriver.get_element(self, _CloseWindowButton, "xpath")
                element.click()
                self.sleep(2)
        else:
            raise TimeoutException("time_out_error")

    def elementClick(self, locator, locatorType):
        try:
            element = WebDriver.get_element(self, locator, locatorType)
            element.click()
            logging.info("Clicked on element with locator: " + locator +
                         " locatorType: " + locatorType)
        except:
            logging.info("Cannot click on the element with locator: " + locator +
                         " locatorType: " + locatorType)

    def click_plus_button_to_expand_category(self, categoryName):
        _expandButton = "//a[contains(text(),'" + categoryName + "')]/preceding-sibling::span[contains(@class,'CLOSE')]"
        if Services.is_element_present(self, _expandButton) is True:
            element = WebDriver.get_element(self, _expandButton, "xpath")
            element.click()
            self.sleep(2)
        else:
            raise TimeoutException("time_out_error")

    def verify_product_in_cart(self, productAmount):
        """productAmount is not itemsAmount"""
        _product = "//td[@class='cart_product']"
        _element = self.driver.find_elements_by_xpath(_product)
        _productAmount = len(_element)
        assert productAmount == _productAmount

    def verify_text_present_on_page(self, textToVerify):
        src = self.driver.page_source
        assert (textToVerify in self.driver.page_source)

    def verify_text_Not_present_on_page(self, textToVerify):
        src = self.driver.page_source
        assert (textToVerify in src) is False

    def compare_actual_items_with_heading(self, textToVerify):
        try:
            itemsPath = "//div[@class='product-image-container']"
            elementLen = len(self.driver.find_elements_by_xpath(itemsPath))
            newTextToVerify = str.replace(textToVerify, "X", str(elementLen))
            self.verify_text_present_on_page(newTextToVerify)
        except NoSuchElementException:
            raise TimeoutException("time_out_error")

    def click_on_item_quickview(self, itemNumber):
        itemElement = "(//a[@class='product_img_link'])[" + str(itemNumber) + "]"
        element = WebDriver.get_element(self, itemElement, "xpath")
        element.click()
        self.sleep(5)

    def click_activate_quick_menu(self, itemNumber):
        itemElement = "(//span[@class = 'available-now'])[" + str(itemNumber) + "]"
        element = WebDriver.get_element(self, itemElement, "xpath")
        action = ActionChains(self.driver)
        coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
        action.move_by_offset(coordinates['x'], coordinates['y'])
        action.move_to_element(element)
        action.click_and_hold(element)
        self.sleep(1)
        action.release(element)
        action.perform()
        """element.click()"""
        self.sleep(2)

    def switch_to_iframe(self):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        """
        freameEl = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to_frame(freameEl)

    def move_to_item_img(self):
        element = WebDriver.get_element(self, "//span[@class='available-now']", "xpath")
        coordinates = element.location_once_scrolled_into_view  # returns dict of X, Y coordinates
        self.sleep(4)

    def go_to_item_page(self, itemNumber):
        itemElement = "(//a[@class='product_img_link'])[" + str(itemNumber) + "]"
        element = WebDriver.get_element(self, itemElement, "xpath")
        element.click()
        self.sleep(4)

    def click_on_cart(self):
        element = WebDriver.get_element(self, "//b[contains(text(), 'Cart')]", "xpath")
        element.click()
        self.sleep(4)
