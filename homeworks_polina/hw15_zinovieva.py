import re
from abc import ABC, abstractmethod
import datetime


class Art(ABC):
    def __init__(self):
        self.type = None
        self._author = None
        self.era = None
        self.name = None
        self.place = None
        self._price = None
        self._year = None

    @property
    def date(self):
        if self._year:
            return self._year
        return "So old"

    @date.setter
    def date(self, year):
        self._year = year

    @abstractmethod
    def purchase(self):
        # your money - price
        pass


class Material(Art):
    def __init__(
        self, type="no", author="no", era="no", name="no", place="no", price=0, year=0
    ):
        super().__init__()
        self.type = type
        self._author = author
        self.era = era
        self.name = name
        self.place = place
        self._price = price
        self._year = year

    def purchase(self):
        my_money = 20000
        selling = my_money - self._price
        if selling >= 0:
            return(f"You have bought a painting, now you have {selling} euros")
        else:
            return(
                f"Your account balance will be {selling}. It is < 0. Sorry,next time."
            )

    def __valuation(self):
        # the older the cooler
        today = datetime.date.today()
        today_year = today.year
        val = today_year - self._year
        if val < 500:
            print(f"{val} - Not that valuable")
        else:
            print(f" {val} - Freaking valuable")

    def __count_in_100_years(self):
        today = datetime.date.today()
        today_year = today.year
        res = (today_year + 100) - self._year
        print(f" In 100 years value will be {res}. Consider buying it later.")

    def buy(self, name: str):
        res = self.__count_in_100_years()
        val = self.__valuation()
        return f"{name} wants to buy a painting"


class Spiritual(Art):
    def __init__(
        self, type="no", author="no", era="no", name="no", place="no", price=0
    ):
        super().__init__()
        self.type = type
        self._author = author
        self.era = era
        self.name = name
        self.place = place
        self._price = price

    def purchase(self):
        if self._price <= 0:
            return("You can't buy spiritual art, its priceless")

    def music_in_museum(self):
        author = self._author
        allowed_spir_authors = (
            "Harry Styles, Mozart, Melovin, Diana Ross, Lynyrd Skynyrd"
        )
        res = re.findall(self._author, allowed_spir_authors)
        if res:
            return(f"{res}-allowed music author")
        else:
            return("Don't listen to it")


penitent_magdalene = Material(
    type="paint", author="Titian", name="PenitentMagdalene", price=300000, year=1555
)
penitent_magdalene.purchase()
penitent_magdalene.buy("Polina")
mus = Spiritual(
    type="mus", author="Harry Styles", price=0, name="From the dining table"
)
mus.music_in_museum()
mus.purchase()
