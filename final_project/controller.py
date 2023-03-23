import classes as cl
# import options as opt

# def start():

#     phone_book = cl.PhoneBook()

#     while True:
#         print("\nOptions:")
#         for i, option in enumerate(opt.options, start=1):
#             print(f"{i}: {option}")
        
#         choice = input("\nEnter choice: ")
        
#         match choice:
#             case "1":
#                 phone_book.load_from_file()
#             case "2":
#                 print(phone_book)
#             case "3":
#                 phone_book.add_entry()
#             case "4":
#                 phone_book.search_entries()
#             case "5":
#                 phone_book.edit_entry()
#             case "6":
#                 phone_book.delete_entry()
#             case "7":
#                 phone_book.save_to_file()
#             case "8":
#                 break
#             case _:
#                 print("Invalid choice. Please try again.")


def start():

    global continue_loop 
    continue_loop = True

    def stop_loop():
        global continue_loop
        continue_loop = False
        print("Good bye!")
        
    phone_book = cl.PhoneBook()

    options_dic = {
        "Load phonebook from file":phone_book.load_from_file,
        "Print phonebook":phone_book.print_all,
        "Add new contact":phone_book.add_entry,
        "Find contact":phone_book.search_entries,
        "Edit contact":phone_book.edit_entry,
        "Remove contact":phone_book.delete_entry,
        "Save phonebook to file":phone_book.save_to_file,
        "Quit": stop_loop
    }

    while continue_loop:

        print("\nOptions:")
        for i, option in enumerate(options_dic.keys(), start=1):
            print(f"{i}: {option}")
        
        choice = input("\nEnter choice: ")
        
        match choice:
            case choice if choice.isnumeric() and 0<int(choice)<=len(options_dic):
                key = list(options_dic.keys())[int(choice)-1]
                options_dic[key]()
            case _:
                print("Invalid choice. Please try again.")