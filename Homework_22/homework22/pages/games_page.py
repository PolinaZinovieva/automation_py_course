#//*[@id="rightNav"]/div[1]/a
from Homework_22.homework22.pages.base_page import BasePage
from Homework_22.core.locator import Locator
from Homework_22.Locators.game_locators import GameLocatorCollection



class GamesSupport(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__game_locator = GameLocatorCollection().game_loc()

    def open_game(self):
        self._click(Locator(*self.__game_locator))






