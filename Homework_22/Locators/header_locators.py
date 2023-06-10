class HeaderLocatorsCollection:
    def __init__(self):
        self.__store_locator = ("xpath", "//*[@id='navlink-store'] ")
        self.__search_locator = ('xpath', "//*[@id='SearchLayout']/div[2]/div/input")
        self.__game_locator = ('xpath', "//*[@alt='EA SPORTS™ FIFA 23 Standard Edition']")
        self.__distr_locator = ('xpath', "//*[@id='sitenav-link-1']/a")
        self.__support_locator = ('xpath', "//*[@id='sitenav-link-2']")
        self.__ue_locator = ('xpath',"//*[@id='sitenav-link-4']/a")


    @property
    def store_locator(self):
        return self.__store_locator

    @property
    def search_loc(self):
        return self.__store_locator
    @property
    def game_loc(self):
        return self.__game_locator

    @property
    def distr_loc(self):
        return self.__distr_locator

    @property
    def support_loc(self):
        return self.__support_locator

    @property
    def ue_loc(self):
        return self.__ue_locator




