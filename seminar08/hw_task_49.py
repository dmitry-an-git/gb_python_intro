def tup_to_txt(tup): # converts tupple to string
    txt = ""
    for i in tup:
        txt += i
        txt += ";"
    txt += "\n"
    return txt

def txt_to_tup(txt): # converts string to tupple
    return tuple(txt.split(";")[:-1])

def load_lines(): # reads the file and updates the list with tupples
    print("Reading the DB...", end = " ")
    global lines 
    lines = []
    with open("data.txt", "r") as data:
        lines = data.readlines()
        lines = [txt_to_tup(line) for line in lines]
    print("Done")
    if len(lines)==0:
        print("Warning! The DB is empty!")

def enter_new(): # asks user for prompts and returns a tupple with new info
    # use only 7 chars as tabs shift if more
    name = input("Please enter the first name: ")[:7]
    surname = input("Please enter the second name: ")[:7]
    phone = input("Please enter the phone number: ")[:7]
    return (name,surname,phone)

def add_new(entry): # adds a tupple to the list
    global lines
    lines.append(entry)

def print_line(index, line): # if we need to print some tupple in a nice way
    print(index, end = "\t\t")
    for item in line:
        print(item, end = "\t\t")
    print("")

def print_lines(lst_index=[]): # print all or selected entries from the global list
    global lines
    if len(lines) == 0:
        print("The DB is empty! Nothing to print!")
    else: 
        print("-"*60)
        print("Index\t\tName\t\tSurname\t\tPhone")
        print("-"*60)
        if len(lst_index) == 0:
            for index, line in enumerate(lines):
                print_line(index, line)
        else:
            for index in lst_index:
                print_line(index, lines[index])
        print("-"*60)

def new_db(): # clears the list
    global lines
    lines = []

def search_txt(): # search by keyword 
    global lines
    prompt = input("Please enter the keyword: ")
    result = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == prompt:
                result.append(i)
    result = set(result)
    if len(result) == 0:
        print("Nothing has been found")
    else: 
        print("The following is found:")
        print_lines(result)
    return result

def modify(): # takes the index of the entry and updates it
    global lines
    size = len(lines)
    index = int(input("Please enter the index of the line you want to modify: "))
    if index>size-1:
        return print("Wrong index!")
    else: 
        print("You want to modify the following entry:")
        print_lines([index])
        lines[index] = enter_new()
        print("Done:")
        print_lines([index])

def delete(): # search by keyword and delete
    global lines
    indexes = search_txt()
    if len(indexes) == 0:
        return
    selection = int(input("Please set the index of the line you want to remove: "))
    if selection in indexes:
        lines.pop(selection)
        print("Done")
    else: print("Wrong index")

def save(): # saves the updated list to file
    global lines
    with open("data.txt", "w") as data:
        for i in lines:
            data.write(tup_to_txt(i))
    print("The changes are saved successfully.")

def easter_chuck():
    from random import randint
    index = randint(0,100)
    with open("chuck.txt", 'r') as chuck:
        print(chuck.readlines()[index])
        
def phonebook():
    global lines
    lines = []
    print("="*60)
    print("SuperPhoneBook 5.0b")
    print("="*60)
    load_lines()
    print('The following commands are supported: \n \
          "add"\t- add one entry \n \
          "print"\t- print all entries \n \
          "mod"\t- modify one entry using its index \n \
          "find"\t- search by keyword \n \
          "remove"\t- search by keyword and remove \n \
          "kill"\t- remove all \n \
          "save"\t- save changes to drive \n \
          "format"\t- format C drive \n \
          "quit"\t- exit \n' )
    
    while True:
        #print("="*60)
        command = input("Please enter the command: ")
        if command == "add":
            add_new(enter_new())
        elif command == "print":
            print_lines()
        elif command == "find":
            search_txt()
        elif command == "mod":
            modify()
        elif command == "remove":
            delete()
        elif command == "kill":
            new_db()
        elif command == "save":
            save()
        elif command == "quit":
            break
        elif command == "format":
            print("Just kidding, hehehe, try 'chuck' as a command to get some (un)funny jokes")
        elif command == "chuck":
            easter_chuck()
        else: 
            print("Wrong command!")

phonebook()