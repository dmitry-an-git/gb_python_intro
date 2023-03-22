import classes as cl

cont = cl.Contact("somebody",3333,"ddd")
phone_book = cl.PhoneBook()
phone_book.load_from_file()
print(phone_book)
print(phone_book.super_print([(4,cont),(4,cont)]))
phone_book.edit_entry()
