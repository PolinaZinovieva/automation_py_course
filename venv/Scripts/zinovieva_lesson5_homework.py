# start
# Task 1
first_value = set([7, 2, 1, 8, 3, 4, 126, 1000, 2345])
second_value = set([2, 7, 1, 3, 8, 4, 124, 2345, 126, 678])
print(sorted(first_value.intersection(second_value)))

# Task2
student_grades = {
    "Polina": 88,
    "Mariia": 48,
    "Linda": 46,
    "Petr": 78,
    "Oleksii": 45,
    "Marta": 67.2,
}

count_avg = round((sum(student_grades.values()) / len(student_grades)), 2)
print(count_avg)
for student in student_grades:
    if student_grades[student] > count_avg:
        print(student)

# Task 3
given = {i for i in range(0, 120)}
print(len(given))

# Task 4
numeric_list1 = set()
numeric_list2 = set()
while len(numeric_list1) < 5:
    iteration1 = int(input("Enter number for your FIRST numeric list"))
    numeric_list1.add(iteration1)
while len(numeric_list2) < 5:
    iteration2 = int(input("Enter number for your SECOND numeric list"))
    numeric_list2.add(iteration2)
intersection = sorted(numeric_list1.intersection(numeric_list2))
print(
    f"Your first list is {numeric_list1}\nYour second list is {numeric_list2}\nIntersection is {intersection}"
)

# Task 5
frequency = {}
given_data = [
    "one",
    "two",
    "three",
    "one",
    "four",
    "five",
    "seven",
    "ten",
    "seven",
    "one",
]
for word in given_data:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
new_freq = frequency.items()
print(set(new_freq))
