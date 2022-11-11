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
