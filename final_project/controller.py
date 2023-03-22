import classes as cl
import options as opt

def start():

    phone_book = cl.PhoneBook()

    while True:
        print("\nOptions:")
        for i, option in enumerate(opt.options, start=1):
            print(f"{i}: {option}")
        
        choice = input("\nEnter choice: ")
        
        match choice:
            case "1":
                phone_book.load_from_file()
            case "2":
                print(phone_book)
            case "3":
                phone_book.add_entry()
            case "4":
                phone_book.search_entries()
            case "5":
                phone_book.edit_entry()
            case "6":
                phone_book.delete_entry()
            case "7":
                phone_book.save_to_file()
            case "8":
                break
            case _:
                print("Invalid choice. Please try again.")
