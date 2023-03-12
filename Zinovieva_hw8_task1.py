# Task 1
def input_sides():
    a = float(input(" enter a "))
    b = float(input(" enter b "))
    c = float(input(" enter c "))
    d = float(input(" enter d "))
    print(f"| left side = {a}, - side = {b}, | right side = {c}, _ side = {d}")

    def if_minus():
        if a or b or c or d < 0:
            print("The side cannot be negative,bye!")
            return True

    if if_minus():
        exit()

    def if_rectangle():
        if (
            ((a**2 + b**2) == (c**2 + d**2))
            and (a != b)
            and (c != d)
            and (b == d)
            and (a == c)
        ):
            return True

    if if_rectangle():

        def rec_area():
            S_rec = round((a * b), 2)
            print(f" The rectangle area is {S_rec}")

        rec_area()
    if_rectangle()

    def if_square():
        if (a**2 + b**2) == (c**2 + d**2) and (a == b == c == d):
            return True

    if if_square():

        def sq_message():
            print("This is a square")

        sq_message()
    if_square()

    if not if_square() and not if_rectangle():
        print("no")


input_sides()
