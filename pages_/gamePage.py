from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class GamePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.__oCookiesPageLocator = (By.ID, "backgroundLeftCanvas")

    def click_to_o_cookies_element(self):
        oCookiesElement = self._find_element(self.__oCookiesPageLocator)
        self._click(oCookiesElement)