import classes

options = [
    "Load phonebook from file",
    "Print phonebook",
    "Add new contact",
    "Find contact",
    "Edit contact",
    "Remove contact",
    "Save phonebook to file",
    "Quit"
]

options_dic = {
    "Load phonebook from file":phone_book.load_from_file(),
    "Print phonebook":print(phone_book),
    "Add new contact":phone_book.add_entry(),
    "Find contact":phone_book.search_entries(),
    "Edit contact":phone_book.edit_entry(),
    "Remove contact":phone_book.delete_entry(),
    "Save phonebook to file":phone_book.save_to_file(),
    "Quit": StopIteration
}