phone_book = []
path = "phone.txt"

def open_file():
    with open(path, "r") as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(";")
        contact = {'name':fields[0],
                   'phone':fields[1],
                   'comment':fields[2]}
        phone_book.append(contact)

def save_file():
    with open(path,"w") as file:
        for contact in phone_book:
            line = ';'.join(contact.values())
            file.write(line + '\n')       

def get_phone_book():
    return phone_book

def add_contact(contact: dict):
    phone_book.append(contact)

def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)

def find_contact(prompt: str):
    res = []
    for contact in phone_book:
        for key in contact.values():
            if prompt.lower() in key.lower():
                res.append(contact)
                break
    return res

def remove_contact(index: int):
    phone_book.pop(index)

