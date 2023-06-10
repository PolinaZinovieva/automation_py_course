class SupportLocatorCollection:
    def __init__(self):
        self.__choose_game_locator = ('xpath', "//*[@id='epicGamesReactWrapper']/div/div[1]/div/div[2]/nav/a[1]")
        self.__cokkie_locator = ('xpath', "//*[@id='onetrust-accept-btn-handler']")

    def choose_game_loc(self):
        return self.__choose_game_locator

    def cookie_loc(self):
        return self.__cokkie_locator