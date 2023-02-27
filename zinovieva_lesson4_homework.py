# start
# Empty list
note_list = []
# adding a greeting with an instruction
print(
    "Hello,human! I am a non-binary artificial intelligence-Krajta.\nTo communicate with me in a way I\
 personally find appropriate use:\n\
\t-add to add a note->'enter'-> type your note\n\
\t-earliest to sort from earliest to latest->'enter'\n\
\t-latest to sort from latest to earliest->'enter'\n\
\t-longest to sort from longest to shortest->'enter'\n\
\t-shortest to sort from shortest to longest->'enter'\n\
\t-exit to abandon me forever->'enter'\n\
You better add at least 2 notes before you start playing with me or you will feel blue"
)

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
            print("Add at least 2 notes, ředkvičky!")
    # sorting from latest to earliest
    elif iteration == "latest":
        sorted_list = note_list
        sorted_list.reverse()
        if len(sorted_list) >= 2:
            print(sorted_list)
        else:
            print("Add at least 2 notes, ředkvičky!")
    # sorting from longest to shortest
    elif iteration == "longest":
        list_by_length = sorted(note_list, key=len, reverse=True)
        # adding restriction (must be at least 2 notes)
        if len(list_by_length) >= 2:
            print(list_by_length)
        else:
            print("Add at least 2 notes, ředkvičky!")
    # sorting from shortest to longest
    elif iteration == "shortest":
        list_by_short = sorted(note_list, key=len)
        # adding restriction (must be at least 2 notes)
        if len(list_by_short) >= 2:
            print(list_by_short)
        else:
            print("Add at least 2 notes, ředkvičky!")
    # exiting the program
    elif iteration == "exit":
        print("How lucky I am to have sth that makes saying goodbye so hard...")
        break
    # a pipeline when the user enters sth odd
    else:
        print("What do you want from me,human?")

# end
