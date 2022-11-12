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

    def change_email(self, old_email, new_email):
        for email in self.email:
            if email.value == old_email:
                self.birthday.append(new_email)
                self.birthday.remove(email)
                return True

    def delete_email(self, delete_email):
        for email in self.email:
            if email.value == delete_email:
                self.birthday.remove(email)
                return True