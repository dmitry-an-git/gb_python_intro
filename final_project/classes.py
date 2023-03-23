class Contact:
    def __init__(self, name, phone_number, comment=''):
        self.name = name
        self.phone_number = phone_number
        self.comment = comment
    
    def __str__(self):
        return f"{self.name:<20}{self.phone_number:<20}{self.comment:<20}"
    
    def to_csv(self):
        return f"{self.name};{self.phone_number};{self.comment}"

class PhoneBook:
    def __init__(self, filename = "phonebook.txt"):
        self.contacts = []
        self.filename = filename
        # self.load_from_file()
    
    def __str__(self):
        lst_of_tup=[]
        for i, contact in enumerate(self.contacts, start=1):
            lst_of_tup.append((i,contact))
        return self.super_print(lst_of_tup)
    
    def print_all(self):
        print(self.__str__())
    
    def super_print(self, index_lst: list[tuple]):
        output = ''
        output += '-'*60+'\n'
        for i, contact in index_lst:
            output += f"{i}: {contact}\n"
        output += '-'*60
        return output

    def get_contact_from_user(self):
        name = input("Enter name: ") 
        phone_number = input("Enter phone number: ")
        comment = input("Enter comment: ")
        return Contact(name, phone_number, comment)
    
    def get_valid_index(self, prompt: str):
        while True:
            try:
                index = int(input(prompt))
                if index < 1:
                    print("Index must be positive.")
                elif index > len(self.contacts):
                    print("Index is too large.")
                else:
                    return index
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def add_entry(self):
        contact = self.get_contact_from_user()
        self.contacts.append(contact)
        print("Contact added.")
    
    def search_entries(self):
        keyword = input("Enter keyword: ").lower()
        results = []
        for i, contact in enumerate(self.contacts, start=1):
            if keyword in contact.to_csv().lower():
                results.append((i, contact))
        if len(results) == 0:
            print("No contacts found.")
        else:
            print(self.super_print(results))
    
    def delete_entry(self):
        index = self.get_valid_index("Enter index of contact to remove: ")
        self.contacts.pop(index-1)
        print("Contact removed")
    
    def edit_entry(self):
        index = self.get_valid_index("Enter index of contact to edit: ")
        old_contact = self.contacts[index-1]
        list_of_tup = [(index,old_contact)]
        print(f"Current contact: \n{self.super_print(list_of_tup)}")
        new_contact = self.get_contact_from_user()
        self.contacts[index-1] = new_contact
        list_of_tup = [(index,new_contact)]
        print(f"Updated contact: \n{self.super_print(list_of_tup)}")
    
    def save_to_file(self):
        with open(self.filename, "w") as file:
            for contact in self.contacts:
                file.write(f"{contact.to_csv()}\n")
        print("Phone book saved.")
    
    def load_from_file(self):
        self.contacts = []
        try:
            with open(self.filename, "r") as file:
                for line in file.readlines():
                    fields = line.strip().split(";")
                    contact = Contact(*fields)
                    self.contacts.append(contact)
            print("Phone book loaded.")
        except: 
            print("Loading phone book failed.")
        
