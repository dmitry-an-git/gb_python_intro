class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f'{self.name:<20} | {self.phone:<20} | {self.comment:<20}'
    
    def to_str(self):
        return f"{self.name};{self.phone};{self.comment}"

class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.phone_list = []
        self.open()
    
    def open(self):
        with open(self.path, 'r', encoding = "UTF-8") as file:
            data = file.readlines()
        for contact in data:
            new_cont = contact.strip().split(';')
            self.phone_list.append(Contact(*new_cont))  #unpacking!

    def save(self):
        data = '\n'.join([contact.to_str() for contact in self.phone_list])
        with open(self.path, 'w', encoding = "UTF-8") as file:
            file.write(data)

    def new_contact(self, name:str, phone: str | int, comment: str):
        self.phone_list.append(Contact(name, phone, comment))

    def __str__(self):
        result = ''
        for contact in self.phone_list:
            result += f'{contact}\n'
        return result[:-2]
    
    def search(self, keyword: str):
        result = []
        for contact in self.phone_list:
                if keyword.lower() in contact.to_str():
                    result.append(f'{contact}')
        return "\n".join(result)
    
    def change(self, index:int, name:str, phone:str, comment:str):
        name = name if name != '' else self.phone_list[index].name 
        phone = phone if phone != '' else self.phone_list[index].phone 
        comment = comment if phone != '' else self.phone_list[index].comment
        self.phone_list[index] = Contact(name,phone,comment)

    def delete(self, index: int):
        self.phone_list.pop(index)

    def main_menu(self):
        return '''Main menu:
            1. Показать
            2. Создать
            3. Найти
            4. Изменить
            5. Удалить
            6. Сохранить книгу
            7. Выйти'''