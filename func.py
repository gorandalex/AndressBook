from AddressBook import AddressBook
from class_address import Address
from class_birthday import Birthday
from Record import Record


def corrector(handler):
    def wrapper(*args, **kwargs):
        try:
            result = handler(*args, **kwargs)
            return result
        except KeyError:
            return 'Enter user name.'
        except ValueError as e:
            return e.args[0]
        except IndexError:
            return 'Give me name and phone'
        except TypeError:
            return 'Give me name and phone'
    return wrapper
@corrector
def hello():
    return "Hello! How can I help you?"

@corrector
def add_new_contact(data):
    name, phone = create_data(data)
    record_add = Record(name.lower())
    record_add.add(phone)
    addressbook.add_record(record_add)
    return f'New contact {name} : {phone}'

@corrector
def delete(data):
    name, phone = create_data(data)
    record_delete = addressbook.data[name]

    if record_delete.delete_phone(phone) is True:
        return f'{name} : {phone} has been deleted'
    else:
        return 'The phone number not exist'

@corrector
def add_phones(data):
    name, phone = create_data(data)
    record_add_phones = addressbook.data[name]
    record_add_phones.add_phone(phone)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].phones))}"

@corrector
def add_emails(data):
    name, email = create_email(data)
    record_add_emails = addressbook.data[name]
    record_add_emails.add_email(email)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].email))}"

@corrector
def add_birthdays(data):
    name, birthday = create_birthday(data)
    record_add_birthdays = addressbook.data[name]
    record_add_birthdays.add_birthday(birthday)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].birthday))}"

@corrector
def add_address(data):
    name, address = create_address(data)
    record_add_addresses = addressbook.data[name]
    record_add_addresses.add_address(address)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].address))}"

def create_data(data):
    name = data[0]
    phone = data[1]
    if name.isnumeric():
        raise ValueError('Wrong name')
    if not phone.isnumeric():
        raise ValueError('Wrong phone')
    return name, phone

def create_email(data):
    name = data[0]
    email = data[1]
    if name.isnumeric():
        raise ValueError('Wrong name')
    if not email.isnumeric():
        raise ValueError('Wrong email')
    return name, email

def create_birthday(data):
    name = data[0]
    birthday = data[1]
    if name.isnumeric():
        raise ValueError('Wrong name')
    if not birthday.isnumeric():
        raise ValueError('Wrong birthday')
    return name, birthday

def create_address(data):
    name = data[0]
    address = data[1]
    if name.isnumeric():
        raise ValueError('Wrong name')
    if not address.isnumeric():
        raise ValueError('Wrong address')
    return name, address

addressbook = AddressBook()