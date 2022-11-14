from AddressBook import AddressBook, Record, Address, Birthday


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
    name = create(data)
    record_add = Record(name.lower())
    addressbook.add_record(record_add)
    return f'New contact {name}'

@corrector
def delete(data):
    name = create(data)
    record_delete = addressbook.data[name]
    if record_delete.delete_name(name) is True:
        return f'{name} has been deleted'
    else:
        return 'The phone number not exist'

@corrector
def add_phones(data):
    name, phone = create_1(data)
    record_add_phones = addressbook.data[name]
    record_add_phones.add_phone(phone)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].phones))}"

@corrector
def add_emails(data):
    name, email = create_1(data)
    record_add_emails = addressbook.data[name]
    record_add_emails.add_email(email)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].email))}"

@corrector
def add_birthdays(data):
    name, birthday = create_1(data)
    record_add_birthdays = addressbook.data[name]
    record_add_birthdays.add_birthday(birthday)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].birthday))}"

@corrector
def add_addresses(data):
    name, address = create_address(data)
    record_add_addresses = addressbook.data[name]
    record_add_addresses.add_address(address)
    return f"{addressbook.data[name].name.value} : {list(map(lambda x: x.value, addressbook.data[name].address))}"
# add_address / (data) Maria 080282 м.Київ, в.Гончара




def replace_phone(data):
    data = data.strip().split()
    name = data[0]
    old_phone = data[1]
    new_phone = data[2]
    record = addressbook.data[name]
    record.change_phone(old_phone, new_phone)
    return f'In contact {name} successfully changed phone {old_phone} to {new_phone}'

# replace_phone Yaroslav 050 060

def replace_email(data):
    data = data.strip().split()
    name = data[0]
    old_email = data[1]
    new_email = data[2]
    record = addressbook.data[name]
    record.change_email(old_email, new_email)
    return f'In contact {name} successfully changed email {old_email} to {new_email}'


def replace_birthday(data):
    data = data.strip().split()
    name = data[0]
    old_birthday = data[1]
    new_birthday = data[2]
    record = addressbook.data[name]
    record.change_phone(old_birthday, new_birthday)
    return f'In contact {name} successfully changed birth date {old_birthday} to {new_birthday}'
    

def replace_address(data):
    data = data.strip().split()
    name = data[0]
    old_address = data[1]
    new_address = data[2]
    record = addressbook.data[name]
    record.change_address(old_address, new_address)
    return f'In contact {name} successfully changed address {old_address} to {new_address}'
    

def delete_phone(data):
    data = data.strip().split()
    name = data[0]
    old_phone = data[1]
    record = addressbook.data[name]
    record.delete_phone(old_phone)
    return f'In contact {name} successfully deleted phone {old_phone}'


def delete_email(data):
    data = data.strip().split()
    name = data[0]
    old_email = data[1]
    record = addressbook.data[name]
    record.delete_email(old_email)
    return f'In contact {name} successfully deleted email {old_email}'



def create(data):
    data = data.strip().split()
    name = data[0]
    return name

def create_1(data):
    data = data.strip().split()
    name = data[0]
    data_1 = data[1]
    return name, data_1

def create_2(data):
    data = data.strip().split()
    name = data[0]
    data_1 = data[1]
    data_2 = data[2]
    return name, data_1, data_2

def create_address(data):
    data = data.strip().split()
    name = data[0]
    address = data[1:]
    return name, address

COMMANDS = {
    'hello': hello,
    'add_name': add_new_contact,
    'add_phone': add_phones,
    'delete': delete,
    'add_email': add_emails,
    'add_birthday': add_birthdays,
    'add_addres': add_addresses,
    'delete_birthday':
    'delete_addres':,
    'search_contact':
    'replace_desc_of_note':
    'search_note': addressbook.search_notes_by_tags
    'delete_note': addressbook.remove_note
    'replace_phone': replace_phone,
    'replace_email': replace_email,
    'replace_birthday': replace_birthday,
    'replace_addres': replace_address,
    'delete_phone': delete_phone,
    'delete_email': delete_email,
    'add_note': addressbook.add_note,
    'add_desc_to_note': addressbook.add_desc_to_note,
    'add_tag_to_note': addressbook.add_tag_to_note,
    'search_note_by_tags': addressbook.search_notes_by_tags,
    'search_notes_by_name': addressbook.search_notes_by_name,
    'delete_note': addressbook.remove_note,
    'sort_func': sort_funk.sorting,
    'close': 
}

addressbook = AddressBook()

@corrector
def answer_exit():
    return 'Good bye!'

@corrector
def command_error():
    return 'Wrong command, please try again.'

def get_answer_function(answer):
    return COMMANDS.get(answer, command_error)

@corrector
def run_command(user_command):
    command = user_command
    params = ''
    for key in COMMANDS:
        if user_command.lower().startswith(key):
            command = key
            params = user_command[len(command):]
            break
    if params:
        return get_answer_function(command)(params.strip())
    else:
        return get_answer_function(command)()


def main():
    while True:
        user_command = input('Введіть команду для бота: ')
        answer = run_command(user_command.strip())
        print(answer)
        if answer == 'Good bye!':
            break

if __name__ == '__main__':
    main()
