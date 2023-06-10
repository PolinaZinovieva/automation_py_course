class GameLocatorCollection:
    def __init__(self):
        self.__game_locator = ('xpath', "//*[@id='Games']/div/ul/li[1]/a/div/img")


    def game_loc(self):
        return self.__game_locator
