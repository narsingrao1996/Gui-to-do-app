FILE_PATH = "notes.txt"


def read_mode(file_path = FILE_PATH):

    with open(file_path, "r") as file:
        notes = file.readlines()
    return notes
def write_mode( note_arg , file_path = FILE_PATH):
    with open(file_path , "w") as file:
        file.writelines(note_arg)