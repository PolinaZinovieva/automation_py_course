from abc import ABC, abstractmethod


class DishFactory(ABC):
    _meal_name: str = " "

    @abstractmethod
    def order_dish(self, name: str):
        pass


class AmuseBouche(DishFactory):
    _meal_name = "Bruschetta"

    def __init__(self):
        self.__options = ["Tomato-basil", "Lemongrass-cheese"]
        self.menu_num = 1
        self.price = 20

    @property
    def options(self):
        return self.__options

    def order_dish(self, name: str):
        if name == "Tomato-basil":
            return "Here is your Tomato-basil Bruschetta"
        elif name == "Lemongrass-cheese":
            return "Here is your Lemongrass-cheese Bruschetta"
        else:
            raise Exception("We don't have this option.")


class MainCourse(DishFactory):
    _meal_name = "Varenyky"

    def __init__(self):
        self.__options = ["Potatoes", "Mushrooms"]
        self.menu_num = 2
        self.price = 30

    @property
    def options(self):
        return self.__options

    def order_dish(self, name: str):
        if name == "Potatoes":
            return "Here is your Potato Verenyky"
        elif name == "Mushrooms":
            return "Here is your Mushroom Varenyky"
        else:
            raise Exception("We don't have this option.")


class Dessert(DishFactory):
    _meal_name = "Sorbet"

    def __init__(self):
        self.__options = ["Lime-mint", "Vodka-strawberry"]
        self.menu_num = 3
        self.price = 20

    @property
    def options(self):
        return self.__options

    def order_dish(self, name: str):
        if name == "Lime-mint":
            return "Here is your Lime-mint Sorbet"
        elif name == "Vodka-strawberry":
            return "Here is your Vodka-strawberry Sorbet"
        else:
            raise Exception("We don't have this option.")


class Drinks(DishFactory):
    _meal_name = "Skinny bitch"

    def __init__(self):
        self.__options = ["Classic", "Raspberry-lime"]
        self.menu_num = 4
        self.price = 10

    @property
    def options(self):
        return self.__options

    def order_dish(self, name: str):
        if name == "Classic":
            return "Here is your Classic Skinny Bitch"
        elif name == "Raspberry-lime":
            return "Here is your Raspberry-lime Skinny Bitch"
        else:
            raise Exception("We don't have this option.")


class OrderPart:
    @staticmethod
    def make_order(meal_name: str):
        if meal_name == "Bruschetta":
            return AmuseBouche()
        elif meal_name == "Varenyky":
            return MainCourse()
        elif meal_name == "Sorbet":
            return Dessert()
        elif meal_name == "Skinny bitch":
            return Drinks()
        else:
            raise Exception(
                "We don't have this option. Choose between:Bruschetta,Varenyky,Sorbet and Skinny Bitch!"
            )


# Menu:
# 1.Amuse Bouche - Bruschetta(Tomato-basil and Lemongrass-cheese) - 20 euros
# 2.Main Course - Varenyky(Potatoes and Mushrooms) - 30 euros
# 3.Dessert - Sorbet(Lime-mint and Vodka-strawberry) - 20 euros
# 4. Drinks - Skinny bitch(Classic and Raspberry-lime) - 10 euros

amuse_bouche = OrderPart.make_order("Bruschetta")
print(amuse_bouche.order_dish("Tomato-basil"))
print(amuse_bouche.order_dish("Lemongrass-cheese"))

main_course = OrderPart.make_order("Varenyky")
print(main_course.order_dish("Potatoes"))
print(main_course.order_dish("Mushrooms"))

desserts = OrderPart.make_order("Sorbet")
print(desserts.order_dish("Lime-mint"))
print(desserts.order_dish("Vodka-strawberry"))

drinks = OrderPart.make_order("Skinny bitch")
print(drinks.order_dish("Classic"))
print(drinks.order_dish("Raspberry-lime"))
