from Name import Name
from Note import Notes
from class_birthday import Birthday
from class_num import Phone, Email
from class_address import Address


class Record():
    def __init__(self, name, address = None, phone = None, birthday = None, email = None, note = None):
        self.name = Name(name)

        if address:
            self.address = Address(address)
        else:
            self.address = ''

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = ''

        if email:
            self.email = Email(email)
        else:
            self.email = ''

        if note:
            self.note = Notes(note)
        else:
            self.note = ''

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
