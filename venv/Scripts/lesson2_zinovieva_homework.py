import math

# Task 1
# Name and Last name
first_name = input("Hello!What is your name?")
last_name = input("Great name! And what is your last name?")
age = int(input("Thanks! How old are you?"))
print(
    "Your full name is"
    + " "
    + first_name
    + " "
    + last_name
    + " "
    + ",and your age is"
    + " "
    + str(age)
)


# capitalization of first letters
print(
    (
        "Your full name is"
        + " "
        + first_name
        + " "
        + last_name
        + " "
        + ",and your age is"
        + " "
        + str(age)
    ).title()
)
# upper case
print(
    (
        "Your full name is"
        + " "
        + first_name
        + " "
        + last_name
        + " "
        + ",and your age is"
        + " "
        + str(age)
    ).upper()
)
# lower case
print(
    (
        "Your full name is"
        + " "
        + first_name
        + " "
        + last_name
        + " "
        + ",and your age is"
        + " "
        + str(age)
    ).lower()
)


# repated name
print(first_name*5)


# \n\t
first_name = (
    "\n\t" + input("Sorry, I forgot your name. Enter it again,please!") + "\n\t"
)
print(first_name)


# Task2
# Area of circle and circumference
radius = float(
    input("Enter the radius of some circle in m and I will show you the magic")
)
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print(
    f"The circumference of a circle is  {round(circumference,2)} m, and the area is  {round(area,2)} sq m!"
)


# Task4
dollar_rate = 36.42
hryvnias_to_convert = int(input("Enter the amount of hryvnias you want to covert:"))
converter_logic = hryvnias_to_convert / dollar_rate
print(f"{hryvnias_to_convert} hryvnias are {round(converter_logic,2)} dollars ")
