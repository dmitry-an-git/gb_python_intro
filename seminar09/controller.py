# __all__ = [name for name in dir() if not name.startswith('_')]

import module
import view

def start():
    while True:
        db = module.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                module.open_file()
                view.show_message("File is loaded!")
            case 2:
                module.save_file()
                view.show_message("File is saved!")
            case 3: 
                view.show_contacts(db,"No contacts!")
            case 4:
                module.add_contact(view.add_contact())
            case 5:
                index = view.input_index('Enter the index to update: ')
                replacement_cont = view.change_contact(db,index)
                module.change_contact(replacement_cont,index)
            case 6:
                keyword = view.input_search('Enter the keyword: ')
                res = module.find_contact(keyword)
                view.show_contacts(res,"Nothing is found!")
            case 7:
                break
    
