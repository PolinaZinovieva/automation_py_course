# Task 1

from abc import abstractmethod, ABC


class Dodge(ABC):
    def __init__(self):
        self.model = None
        self.color = None
        self.drive = None
        self.fuel = None
        self.engine = None
        self.price = None
        self.year = None

    def fuel_consumption(self):
        print("Consumption")

    def fuel_type(self):
        print(f" Fuel type is {self.fuel}")

    @abstractmethod
    def crashability(self):
        pass


class Model_details(Dodge):
    def __init__(self):
        super(Model_details, self).__init__()
        self.model = "Dart"
        self.color = "Blue"
        self.drive = "Front-wheel"
        self.fuel = "LPG"
        self.engine = "2.4"

    def fuel_type(self):
        print(f" Fuel type is {self.fuel}")

    def fuel_consumption(self):
        second_fill = 35
        mileage = 240
        print(f"The consumption is {(second_fill / mileage) * 100}")


class Price(Dodge):
    def __init__(self):
        super(Price, self).__init__()
        self.price = 10000
        self.year = 2015

    def type(self):
        print("Multiair")


class Credit(Price):
    def __init__(self):
        super(Credit, self).__init__()
        print(f"{self.price / 12} dollars per month")


model = Model_details()
model.price
