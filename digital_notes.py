from functions import *
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time as a string
formatted_time = now.strftime("%d-%m-%y %H:%M:%S")

print("welcome to digital notes", formatted_time)



while True:
    # Get user action and remove leading/trailing spaces
    user_action = input("type add, show, edit, delete, or exit: ")
    user_action = user_action.strip()

    # Initialize an empty list to store notes
    notes = []

    if user_action.startswith("add"):
        # Get a new note from the user and add a newline character
        note = user_action[4:]

        # Read existing notes from the file
        notes = read_mode()

        # Append the new note to the list of notes
        notes.append(note + "\n")

        # Write the updated notes list back to the file
        write_mode( notes)

    elif user_action.startswith("show"):
        # Read existing notes from the file
        notes = read_mode()

        new_notes = []

        # Remove newline characters from notes and store in new_notes list
        for item in notes:
            new_item = item.strip('\n')
            new_notes.append(new_item)

        # Display the notes with their index
        for index, item in enumerate(new_notes):
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        num = int(user_action[5:])


        # Read existing notes from the file
        notes = read_mode()

        # Get the note number to edit from the user

        num = num - 1

        # Check if the note number is valid
        if 0 <= num < len(notes):
            # Get the new note from the user and add a newline character
            new_note = input("write a new note: ")

            # Update the selected note in the notes list
            notes[num] = new_note + "\n"

            # Write the updated notes list back to the file
            write_mode(notes)
        else:
            print("Invalid note number.")

    elif user_action.startswith("delete"):
        num = int(user_action[7:])
        notes = read_mode()

        # Check if the note number is valid
        if 1 <= num <= len(notes):
            # Remove the selected note from the notes list
            index = num - 1
            remove_notes = notes[index].strip("\n")
            notes.pop(index)

            # Write the updated notes list back to the file
            write_mode(notes)
            message = f"note {remove_notes} deleted from the list"
            print(message)
        else:
            print("Invalid note number.")

    elif user_action == "exit":
        # Exit the loop and end the program
        break

    else:
        print("Invalid entry")
