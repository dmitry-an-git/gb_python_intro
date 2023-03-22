import phone_book
import view
pb = phone_book.PhoneBook('phone.txt')
#pb.new_contact("Ирина Алегрова",88888,"Певица")
# print(pb)
# pb.save()

while True:
    print(pb.main_menu())
    choice = int(input("Please enter selection: "))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            comment = input("Enter comment: ")
            pb.new_contact(name, phone, comment)
        case 3:
            word = input("Enter keyword: ")
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input("Enter index to be modified: "))
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            comment = input("Enter comment: ")
            pb.change(index, name, phone, comment)
        case 5: 
            print(pb)
            index = int(input("Enter index to be deleted: "))
            pb.delete(index)
        case 6: 
            pb.save()
        case 7:
            break
        case _:
            print("Incorrect input! Please try again.")
