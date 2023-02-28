import random

# Task 1
min = random.randrange(60)
print(min)
if min >= 0 and min <= 15:
    print("First quarter")
elif min > 15 and min <= 30:
    print("Second quarter")
elif min > 30 and min <= 45:
    print("Third quarter")
else:
    print("Fourth quarter")


# Task 2
birth_month = int(input("What is your birth month number?"))
if birth_month > 0 and birth_month < 13:
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    if birth_month in winter:
        print("There was snow fallin' outside the window")
    elif birth_month in spring:
        print("Everything was blooming around")
    elif birth_month in summer:
        print("Children were enjoying their summer break")
    else:
        print("Everything around was litting up with bright colours")
else:
    print(" enter values in a range from 1 to 12")


# Task 3
x = random.randint(0, 9999)
devide_by_6 = True
print(x)
if x >= 0 and x < 10:
    if x % 2 == 0 and x % 3 == 0:
        devide_by_6 = True
        print("The number can be devided by 6")
    else:
        print("Cannot devide by 6")
elif x >= 10 and x < 100:
    x = str(x)
    ast_number = int(x[-1])
    first_number = int(x[0])
    sum = last_number + first_number
    if last_number % 2 == 0 and sum % 3 == 0:
        devide_by_6 = True
        print("The number can be devided by 6")
    else:
        print("Cannot devide by 6")
elif x >= 100 and x < 1000:
    x = str(x)
    last_number = int(x[-1])
    first_number = int(x[0])
    second_number = int(x[1])
    sum = last_number + first_number + second_number
    if last_number % 2 == 0 and sum % 3 == 0:
        devide_by_6 = True
        print("The number can be devided by 6")
    else:
        print("Cannot devide by 6")
else:
    x = str(x)
    last_number = int(x[-1])
    first_number = int(x[0])
    second_number = int(x[1])
    third_number = int(x[2])
    sum = last_number + first_number + second_number + third_number
    if last_number % 2 == 0 and sum % 3 == 0:
        devide_by_6 = True
        print("The number can be devided by 6")
    else:
        print("Cannot devide by 6")


# Task 4
x = float(input("Enter x"))
y = float(input("Enter y"))
coordinates = f"Coordinate: ({x}; {y}) - "
if x > 0 and y > 0:
    print(coordinates + "First quarter")
elif y > 0 and x < 0:
    print(coordinates + "Second quarter")
elif y < 0 and x < 0:
    print(coordinates + "Third quarter")
elif x > 0 and y < 0:
    print(coordinates + "Fourth quarter")
elif x == 0 and y != 0:
    print(coordinates + "The value is on y-axis")
elif x != 0 and y == 0:
    print(coordinates + "The value is on x-axis")
else:
    print(coordinates + "The value is at origin")
