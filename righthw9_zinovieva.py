import re


# Task 1
def domains(fily):
    file = open(fily, "r")
    res = file.read()
    output = res.replace(".", "")
    output2 = list(output.split("\n"))
    print(output2)


domains("domains.txt")


# Task 2
file_names = open("names.txt", "w+")
file_names.write("1 Zinovieva Ukraine\n2 Simpson USA\n3 Russo Italy\n4 Sugg UK")
file_names.close()


def names(file2):
    lastname_list = []
    with open(file2, "r") as names:
        for l in names:
            lastname = l.split()[1]
            lastname_list.append(lastname)
        print(lastname_list)


names("names.txt")


# Task 3
def authors(file3):
    with open(file3, "r") as author_dates:
        data = author_dates.readlines()
        authors_list = []
        for l in data:
            text = l.strip()
            if not text.isnumeric() and text:
                res = re.search(r"(\d{1,2}(st|nd|rd|th) \w+ \d{4})", text)
                if res:
                    authors_list.append({"date": res.group(1)})
        print(authors_list)


authors("authors.txt")
