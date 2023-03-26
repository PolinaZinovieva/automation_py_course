# Task 1
import re


def w(text):
    res = re.fullmatch(r"^(\w|\s)+\Z", text)

    # res2 = re.findall("\W+", data)
    if res:
        print("The string meets the requirements")
    else:
        print("The string contains smth except the A-Z,a-z,0-9,_")


w("Hello124_")


# Task 2
def remove_brackets(text2):
    res = re.sub(r"\([^()]*\)", "", text2)
    print(res)


remove_brackets("hello(.com), hola(.net), bye(.ua)")


# Task 3
def upper_space(text):
    # res = re.sub(r'([A-ZА-Я])'," ", text).split()
    res = re.sub(r"([A-ZА-Я])", r" \1", text)
    print(res)


upper_space("HelloПривітGutenTag!")
