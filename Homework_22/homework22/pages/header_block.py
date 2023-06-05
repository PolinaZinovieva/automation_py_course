from Homework_22.homework22.pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver import Keys


class HeaderBlock(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.__store =('xpath', "//*[@id='navlink-store'] ")
        self.__store_search = ('xpath', "//*[@id='SearchLayout']/div[2]/div/input")
        self.__game = ('xpath', "//*[@alt='EA SPORTS™ FIFA 23 Standard Edition']")
        self.__distr = ('xpath', "//*[@id='sitenav-link-1']/a")
        self.__support = ('xpath', "//*[@id='sitenav-link-2']")
        self.__ue=('xpath',"//*[@id='sitenav-link-4']/a")









    def open_store(self, name):
        locator = ('xpath', f"//*[@id='navlink-{name}'and @tabindex='-1']")
        element = self._wait_until_el_appears(locator)
        element.click()





    def find_game(self):
        element = self._wait_until_el_appears(self.__store_search)
        element.send_keys("FIFA 23")
        element.send_keys(Keys.ENTER)

    def open_distribution(self):
        element = self._wait_until_el_appears(self.__distr)
        element.click()


    def open_support(self):
        element = self._wait_until_el_appears(self.__support)
        element.click()

    def open_ue(self):
        element = self._wait_until_el_appears(self.__ue)
        element.click()











