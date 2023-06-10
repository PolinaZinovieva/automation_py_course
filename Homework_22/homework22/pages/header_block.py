from Homework_22.homework22.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Keys
from Homework_22.homework22.pages.support_page import ElementsSP
from Homework_22.core.locator import Locator
from Homework_22.Locators.header_locators import HeaderLocatorsCollection

class HeaderBlock(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__store = HeaderLocatorsCollection().store_locator
        self.__store_search = HeaderLocatorsCollection().search_loc
        self.__game = HeaderLocatorsCollection().game_loc
        self.__distr = HeaderLocatorsCollection().distr_loc
        self.__support = HeaderLocatorsCollection().support_loc
        self.__ue = HeaderLocatorsCollection().ue_loc


    def open_store(self):
        self._click(Locator(*self.__store))


    def find_game(self):
        element = self._wait_until_el_appears(Locator(*self.__store_search))
        element.send_keys("FIFA 23")
        element.send_keys(Keys.ENTER)

    def open_distribution(self):
        self._click(Locator(*self.__distr))

    def open_support(self):
        self._click(Locator(*self.__support))
        return ElementsSP(self._driver)

    def open_ue(self):
        self._click(Locator(*self.__ue))













