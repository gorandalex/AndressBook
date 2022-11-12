from Name import Name
from Note import Note
from class_birthday import Birthday
from class_num import Phone, Email
from class_address import Address


class Record():
    def __init__(self, name, phone = None):
        self.name = Name(name)

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

       

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        phone_obj = Phone(old_phone)    
        if phone_obj in self.phones:
            self.phones[self.phones.index(phone_obj)] = Phone(new_phone)
            return True

    def delete_phone(self, phone):
        phone_obj = Phone(phone)    
        if phone_obj in self.phones:
            self.phone.remove(phone_obj)
            return True
    

    def add_email(self, email):
        if self.email is None:
            self.email = Email(email)
        else:
            raise ValueError("""This contact {self.name} 
            already have date of birthday: {self.birthday}
            if you want to change tis date try "change_email | new_email"
            """)


    def add_birthday(self, birthday):
        self.birthday.append(Birthday(birthday))

    def change_birthday(self, old_birthday, new_birthday):
        for birthday in self.birthday:
            if birthday.value == old_birthday:
                self.add_birthday(new_birthday)
                self.birthday.remove(birthday)
                return True

    def delete_birthday(self, delete_birthday):
        for birthday in self.birthday:
            if birthday.value == delete_birthday:
                self.birthday.remove(birthday)
                return True




    def add_address(self, address):
        self.address.append(Address(address))

    def change_address(self, old_address, new_address):
        for address in self.address:
            if address.value == old_address:
                self.add_address(new_address)
                self.address.remove(address)
                return True

    def delete_address(self, delete_address):
        for address in self.address:
            if address.value == delete_address:
                self.address.remove(address)
                return True   
