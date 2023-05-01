# Task1


def singleton(_class):
    def inner(*args):
        if not hasattr(_class, "instance"):
            setattr(_class, "instance", _class(*args))
        return getattr(_class, "instance")

    return inner


@singleton
class Student:
    def __init__(self, avg_grade: float, subject: str, name: str):
        self.__grade = avg_grade
        self.subject = subject
        self.creds = name

    def Logic(self):
        if self.__grade < 60:
            print(f"{self.__grade} is not good,{self.creds} Learn {self.subject} more")
        else:
            print("Ok,good")


Student1 = Student(88.89, "Math", "Mariia")
Student2 = Student(10.0, "English", " Andrew")
print()
