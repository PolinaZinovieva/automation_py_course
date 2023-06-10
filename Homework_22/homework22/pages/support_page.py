from Homework_22.homework22.pages.base_page import BasePage
from Homework_22.homework22.pages.games_page import GamesSupport
from Homework_22.core.locator import Locator
from Homework_22.Locators.support_locators import SupportLocatorCollection


class ElementsSP(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.__choose_game = SupportLocatorCollection().choose_game_loc()
        self.__cookie = SupportLocatorCollection().cookie_loc()

    def click_game(self):
        self._click(Locator(*self.__cookie))

        self._click(self.__choose_game)
        return GamesSupport(Locator(*self._driver))

