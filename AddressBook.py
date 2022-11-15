from datetime import date
from collections import UserDict
from re import search, match
import pickle

class AddressBook(UserDict):

    def __init__(self, data = None):
        super().__init__(data)
        self.notes = []

    def add_record(self, record):
        self.data[record.name.value] = record
        return 'Record was added'

    def return_record_by_name(self, name):
        return self.data[name]

    def remove_record(self, record):
        del self.data[record.name.value]
        return 'Record was deleted'

    def search_contact(self, name):
        if name in self.data:
            record = self.data[name]
            return f'{record}'
        else:
            return 'Contact not found'


    def add_note(self, note, description = None, tag = None):
        self.notes.append(Note(note, description, tag.lower() if tag else ''))

    def add_desc_to_note(self, note):
        for book_note in self.notes:
            if note.startswith(book_note.note):
                description = note[len(book_note.note):].strip()
                book_note.description = description
                return 'description is added'
        return 'Note not found'

    def add_tag_to_note(self, note):
        for book_note in self.notes:
            if note.startswith(book_note.note):
                tags = note[len(book_note.note):].strip()
                lst_tags = book_note.tags.split(',')
                lst_tags.extend([tag for tag in tags.lower().split(' ')])
                lst_tags.sort()
                book_note.tags = ','.join(tag for tag in lst_tags if tag != '')
                return 'Tags is added'
        return 'Note not found'

    def search_notes_by_tags(self, tags):
        tags_answer = []
        lst_tags = tags.split(' ')
        for book_note in self.notes:
            if set(book_note.tags.split('#')) & set(lst_tags) == set(lst_tags):
                tags_answer.append(book_note)
        return tags_answer

    def sort_notes_by_tags(self):
        self.notes = sorted(self.notes, key=lambda x: x.tags)

    def search_notes_by_name(self, note):
        for book_note in self.notes:
            if book_note.note == note:
                return book_note

    def remove_note(self, note):
        book_note = self.search_notes_by_name(note)
        if book_note:
            self.notes.remove(book_note)
            return 'Note was removed'
        else:
            return 'Note not found'

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, "rb") as file:
            content = pickle.load(file)
        return content


class Record():
    def __init__(self, name, phone = None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.email = None
        self.birthday = None
        self.address = None
       
    def __repr__(self) -> str:
        phones = ', '.join([phone.value for phone in self.phones if not phone.value is None])
        return f'{self.name} : phones {phones}, email: {self.email}, birthday: {self.birthday}, address: {self.address}'

    def add_phone(self, phone):
        for rec_phone in self.phones:
            if rec_phone.value == phone:
                raise ValueError("""This contact {self.name} 
                            already have phone : {phone}
                            if you want to change tis date try "change_email | new_email"
                            """)                
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.append(Phone(new_phone))
                self.phones.remove(phone)
                return True

    def delete_phone(self, phone):
        phone_obj = Phone(phone)    
        if phone_obj in self.phones:
            self.phone.remove(phone_obj)
            return True
    
    def delete_name(self, name):
        name_obj = Name(name)
        if name_obj in AddressBook.data[name]:
            AddressBook.data[name].remove(name_obj)


    def add_email(self, email):
        if self.email is None:
            self.email = Email(email)
        else:
            raise ValueError("""This contact {self.name} 
            already have date of email: {self.email}
            if you want to change tis date try "change_email | new_email"
            """)

    def change_email(self, old_email, new_email):
        if old_email == self.email.value:
            self.email = Email(new_email)
            return True

    def delete_email(self, delete_email):
        if delete_email == self.email.value:
            self.email = None
            return True

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

class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    def __repr__(self) -> str:
        return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class Address(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
        self.value = self.check_address(value)

    @staticmethod
    def check_address(value):
        clean_address = (
                        value.strip()
                        .replace("(", "")
                        .replace(")", "")
                        .replace("-", "")
                        .replace(" ", "")
                        .replace(",", " ")
                    )
        value = search(r"\d{5}\ \м.\w+\ \в.\w+(\d+|\D+)+", clean_address)
        if not value:
            raise ValueError(f"Invalide address format {clean_address}. Address format should be IIII, м.Місто, в.Вулиця, дод.записи")
        return str(value)

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    @Field.value.setter
    def value(self, value):
        self._value = self.check_date(value)

    @staticmethod
    def check_date(value):
        value = value.strip()

        for separator in (".", ",", "-", ":", "/"):
            value, *args = value.split(separator)

            if args:
                break

        if not args or len(args) > 2:
            raise ValueError("Invalide date format. Date format should be YYYY.MM.DD or DD.MM.YYYY.")

        if int(value) > 31:
            return date(int(value), int(args[0]), int(args[1]))

        return date(int(args[1]), int(args[0]), int(value))

class Phone(Field):

    def __repr__(self):
        return self.value


    @Field.value.setter
    def value(self, value:str):
        if not all((value.startswith('+380'), len(value) == 13, value[1:].isdigit())):
            raise ValueError("""Phone number {value} is not valid, 
            please enter correcct phone '+380XXXXXXX'""")
        self._value = value



class Email(Field):
    
    @Field.value.setter
    def value(self, value:str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (match(regex, value)):
            raise ValueError(""""Email {value} is not valid,
            please enter correct email.
            Example of emails: my.ownsite@our-earth.org
                                ankitrai326@gmail.com""")
        self._value = value

class Name(Field):
    pass

class Note:
    def __init__(self, note, description = None, tags= None):
        self.__note = None
        self.note = note
        self.description = description
        if tags:
            self.tags = ','.join((tag for tag in tags.split(' ')))
        else:
            self.tags = ''

    @property
    def note(self):
        return self.__note        

    @note.setter
    def note(self, note):
        self.__note = note

    def __repr__(self) -> str:
        return f'{self.__note}: {self.description} ({self.tags})'
          
