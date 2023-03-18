import text_fields

def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split("\n"))
    while True:
        choice = input("Please enter the number: ")
        if choice.isnumeric() and 0 < int(choice) < length_menu:
            return int(choice)
        else:
            print(f"Wrong choice! Enter the number from 1 to {length_menu-1}")

def show_contacts(book: list, error_message: str):
    if not book:
        print(error_message)
        return
    else:
        for i, contact in enumerate(book):
            print(f"{i}. {contact.get('name'):<20}"
                  f"{contact.get('phone'):<20}"
                  f"{contact.get('comment'):<20}")

def add_contact() -> dict:
    name = input("Enter the name: ")
    phone = input("Enter the phone: ")
    comment = input("Enter the comment: ")
    return {'name': name, 'phone': phone, 'comment': comment}

def input_index(message: str) -> int:
    return int(input(message))

def input_search(message: str) -> str:
    return input(message)

def change_contact(book: list, index: int):
    print("Please enter new data or leave the fields blank if no changes")
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}

def show_message(message:str):
    print('-'*len(message))
    print(message)
    print('-'*len(message))
