# Task 2
import random
import string

names = [
    "anomatopoeia",
    "remuneration",
    "anonymous",
    "phenomenon",
    "rotavator",
    "mellifluous",
]
domains = ["com", "org", "net", "int", "gov", "boo"]


def email_creator(names, domains):
    number = random.randint(100, 1000)
    string_r = "".join(random.sample((string.ascii_lowercase), 7))
    name_r = "".join(random.sample(names, 1))
    domains_r = "".join(random.sample(domains, 1))

    def email_assembling():
        print(f"Your email is: {name_r}{number}@{string_r}.{domains_r}")

    email_assembling()


email_creator(names, domains)

# Lambda Tasks
# Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.
s1 = {1, 2, 3, 4, 99, 6}
s2 = {4, 6, 3, 7, 8, 99}
intersec = lambda x, y: x.intersection(y)
print(intersec(s1, s2))

# Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда
string = input("enter some string")
if_number = lambda x: print("yes") if x.isdigit() else print("no")
print(if_number(string))
