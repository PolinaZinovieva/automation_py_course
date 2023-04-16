# Task 1

import csv

# Step 1 read the file and return the list to use it later
def csv_file(file):
    a = []
    with open(file, "r") as file_csv:
        csv_read = csv.reader(file_csv)
        for l in csv_read:
            a.append(l)
        print(f"This is regular list{a}")
    return a


# Step 2 edit the file
def csv_edit(file, text1, text2, text3):
    with open(file, mode="w") as edit_csv:
        csv_ed = csv.writer(edit_csv, delimiter=",")
        csv_ed.writerow(text1)
        csv_ed.writerow(text2)
        csv_ed.writerow(text3)


# Call the functions
csv_edit(
    "new.csv",
    ["Love", "Pet", "Popo"],
    ["Like", "Dog", "Pop"],
    ["Hate", "Cat", "Popopo"],
)
csv_file("new.csv")

# Adding more text via console
file = csv_file("new.csv")
additional_t = []
while len(additional_t) < 3:
    additional_i = input("Enter value")
    additional_t.append(additional_i)
print(f"You added {additional_t} to the list")


for l in additional_t:
    file.append(l)

print(f"This is appended list {file}")

# Adding all the changes to another list
with open("another.csv", mode="w") as another_csv:
    write = csv.writer(another_csv, delimiter=",")
    write.writerows(file)


# Task 2

def sq():
    counter = 0
    while counter < 100000:
        yield counter ** 2
        counter += 1
s = sq()
for i in s:
    print(i)


