# Задача No49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


# the code uses list "lines" that contains tupples with telephone entries as main DB
# the DB can be read from and saved to a txt file that holds the data in a semicolon-separated format
# the code works with the list and saves is to the drive only when requested

def tup_to_txt(tup): # converts tupple to string
    txt = ""
    for i in tup:
        txt += i
        txt += ";"
    txt += "\n"
    return txt

def txt_to_tup(txt): # converts string to tupple
    return tuple(txt.split(";")[:-1])

def load_lines(): # reads the file and repopulates the list with tupples accordingly
    print("Reading the DB...", end = " ")
    global lines 
    lines = []
    with open("data.txt", "a+") as data:
        data.seek(0) # if there is no file a+ creates it, if there is one, we need to go to the beginning
        lines = data.readlines()
        lines = [txt_to_tup(line) for line in lines]
    print("Done")
    if len(lines)==0:
        print("Warning! The DB is empty!")

def enter_new(): # asks user for a prompt and returns a tupple with new info
    # use only 7 chars as tabs shift if more
    name = input("Please enter the first name: ")[:7]
    surname = input("Please enter the second name: ")[:7]
    phone = input("Please enter the phone number: ")
    return (name,surname,phone)

def add_new(entry): # adds a tupple to the list
    global lines
    lines.append(entry)
    print("Done")

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

def kill(): # clears the list / removes all entries
    global lines
    lines = []
    print("Done")

def search_one(keyword, string): # technical function to check if a keyword is in a string
    keyword = keyword.lower()
    string = string.lower()
    ans = False
    for i in range(len(string)-len(keyword)+1):
        for j in range(len(keyword)):
            if keyword[j] == string[i+j]:
                ans = True
            else: 
                ans = False
                break
        if ans == True:
            break
    return ans

def search_txt(): # search by keyword in the list of tupples
    global lines
    prompt = input("Please enter the keyword: ")
    result = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if search_one(prompt, lines[i][j]):
                result.append(i)
    result = set(result)
    if len(result) == 0:
        print("Nothing has been found")
    else: 
        print("The following has been found:")
        print_lines(result)
    return result

def input_index(wording): # checks for correct input of indexes by the user
    while True:
        try:
            index = int(input(wording))
            break
        except:
            pass
    return index

def modify(): # takes the index of one entry from the user and updates it
    global lines
    size = len(lines)
    index = input_index("Please enter the index of the line you want to modify: ")
    if index>size-1:
        return print("Wrong index!")
    else: 
        print("You want to modify the following entry:")
        print_lines([index])
        lines[index] = enter_new()
        print("Done:")
        print_lines([index])

def remove(): # search by keyword and delete
    global lines
    indexes = search_txt()
    if len(indexes) == 0:
        return
    selection = input_index("Please set the index of the line you want to remove: ")
    if selection in indexes:
        lines.pop(selection)
        print("Done")
    else: print("Wrong index")

def save(): # saves the updated list to file
    global lines
    with open("data.txt", "w") as data:
        for i in lines:
            data.write(tup_to_txt(i))
    print("The changes have been saved successfully.")

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
          "search"\t- search by keyword \n \
          "remove"\t- search by keyword and remove \n \
          "kill"\t- remove all \n \
          "save"\t- save changes to drive \n \
          "format"\t- format C drive \n \
          "quit"\t- quit the app \n' )
    
    while True:
        #print("="*60)
        command = input("Please enter the command: ")
        if command == "add":
            add_new(enter_new())
        elif command == "print":
            print_lines()
        elif command == "search":
            search_txt()
        elif command == "mod":
            modify()
        elif command == "remove":
            remove()
        elif command == "kill":
            kill()
        elif command == "save":
            save()
        elif command == "quit":
            break
        elif command == "format":
            print("Just kidding, hehehe, try 'chuck' as a command to get some random (un)funny jokes")
        elif command == "chuck":
            easter_chuck()
        else: 
            print("Wrong command!")

phonebook()