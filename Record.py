from Name import Name
from Note import Note
from class_birthday import Birthday
from class_num import Phone, Email
from class_address import Address


class Record():
    # def __init__(self, name, address = None, phone = None, birthday = None, email = None, note = None):
    def __init__(self, name, phone = None):
        self.name = Name(name)

        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

       # if address:
        #     self.address = Address(address)
        # else:
        #     self.address = ''

        # if birthday:
        #     self.birthday = Birthday(birthday)
        # else:
        #     self.birthday = ''

        # if email:
        #     self.email = Email(email)
        # else:
        #     self.email = ''


