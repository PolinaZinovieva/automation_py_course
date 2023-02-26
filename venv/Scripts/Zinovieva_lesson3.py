import random

# Task 1
while True:
    min = random.randrange(60)
    print(min)
    first_quarter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    second_quarter = [16, 17, 18, 19, 20, 21, 21, 23, 24, 25, 26, 27, 28, 29, 30]
    third_quarter = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    if min in first_quarter:
        print("First quarter")
    elif min in second_quarter:
        print("Second quarter")
    elif min in third_quarter:
        print("Third quarter")
    else:
        print("Fourth quarter")
    break


# Task 2
while True:
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
    elif birth_month <= 0 or birth_month >= 13:
        print(" enter values in a range from 1 to 12")
    break

# Task 3
x = random.randint(0, 9999)
devide_by_6 = True
print(x)
while True:
    if x >= 0 and x < 10:
        if x % 2 == 0 and x % 3 == 0:
            devide_by_6 = True
            print("The number can be devided by 6")
        else:
            print("Cannot devide by 6")
    elif x >= 10 and x < 100:
        x = str(x)
        last_number = int(x[-1])
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
        break
# Task 4
while True:
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
    elif x == 0 and y == 0:
        print(coordinates + "The value is at origin")
    break
