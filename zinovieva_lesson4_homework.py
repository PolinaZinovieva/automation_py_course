# start
# Empty list
note_list = []

# cycle while
while True:
    iteration = input("Enter:add,earliest,latest,longest,shortest,exit")
    # add a note
    if iteration == "add":
        notes = input("Add your note")
        note_list.append(notes)
        print("added" + " " + notes)
    # sorting from earliest to latest
    elif iteration == "earliest":
        # adding restriction (must be at least 2 notes)
        if len(note_list) >= 2:
            print(note_list)
        else:
            print("Add at least 2 notes")
    # sorting from latest to earliest
    elif iteration == "latest":
        sorted_list = sorted(note_list, reverse=True)
        # adding restriction (must be at least 2 notes)
        if len(sorted_list) >= 2:
            print(sorted_list)
        else:
            print("Add at least 2 notes")
    # sorting from longest to shortest
    elif iteration == "longest":
        list_by_length = sorted(note_list, key=len, reverse=True)
        # adding restriction (must be at least 2 notes)
        if len(list_by_length) >= 2:
            print(list_by_length)
        else:
            print("Add at least 2 notes")
    # sorting from shortest to longest
    elif iteration == "shortest":
        list_by_short = sorted(note_list, key=len)
        # adding restriction (must be at least 2 notes)
        if len(list_by_short) >= 2:
            print(list_by_short)
        else:
            print("Add at least 2 notes")
    # exiting the program
    elif iteration == "exit":
        print("Hooray!Bye!")
        break
    # a pipeline when the user enters sth odd
    else:
        print("What do you want from me,human?")

# end
