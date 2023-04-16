from random import randint


# Task 1
def name(function):
    def wrapper(*args, **kwargs):
        print(f"The {function.__name__} function was used")
        return function(*args, **kwargs)

    return wrapper


@name
def calc(a, b):
    return (a + b - a) * b


@name
def divide(a, b, c):
    return round(a / b / c, 3)


print(calc(3, 5))
print(divide(6, 7, 9))

# Task 2
numbs = [randint(1, 10) for i in range(100)]
count_dict = {n: numbs.count(n) for n in set(numbs)}
for n, count in count_dict.items():
    print(f"Number {n} was detected {count} times ")
