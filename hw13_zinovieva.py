# Task 1


class Lottie:
    def __init__(self, breed, character, age):
        self.breed = breed
        self.character = character
        self.age = age

    def fave_toys(self):
        rope = 2
        ball = 3
        favourite = ball - rope
        print(f"Lottie`s favourite toy for {self.age} is {favourite}")

    @staticmethod
    def activity(level):
        print(f"Lottie`s running skill is at level {level}")


Lottie.activity(10)

# Task 2


# The data is completely fictional
class Wargaming:
    game = "World of Tanks"
    value = 2399988939493949

    def __init__(self, developers, qa, designers, artists):
        self.developers = developers
        self.qa = qa
        self.designers = designers
        self.artists = artists
        print(f"We have {developers + qa + designers + artists} employees")

    def qas(self):
        qa_list = []
        qa_list.append(self.qa)
        print(qa_list)

    @classmethod
    def net_value(cls):
        print(f"{cls.game} net value is {cls.value}")


Wargaming.net_value()
