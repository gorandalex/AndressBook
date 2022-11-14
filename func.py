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
    name, phone = create_1(data)
    record_add = Record(name.lower(), phone)
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
    name, data_1 = create_1(data)
    record_add_phones = addressbook.data[name]
    record_add_phones.add_phone(data_1)
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
# add_address / (data) Maria 080282 м.Київ, в.Гончара


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

# @corrector
def find(text):
    text = create(text)
    print(text)
    answer_records = ''
    list = addressbook.find_records_by_text(text)
    print(list)
    for record in list:
        answer_records += record + '\n'
    return answer_records

# def find(data):
#     data = create(data)
#     print(data)
#     for users in addressbook.values():
#         contacts = [phone.value for phone in users.phones]
#         #contacts1 = [name.value for phone in users.name]
#         for el in contacts:
#             if data in str(el):
#                 return users
#         if data in users.name.value:
#             return users
def searcher(text):
    text = create(text)
    for users in addressbook.values():
        for el in users.phones:
            if text in el:
                print(users)
        if text in users.name.value:
            print(users)

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

instructions = """hello (print instructions)
add / name / phone
delete / name
add_phone / name / new_phone
add_email / name / new_email
add_birthday / name / new_birthday
add_address / name / address

delete_birthday / name /old_birthday
delete_addres / name /old_addres
search_contact / name
replace_desc_of_note
search_note (by name)
delete_note (by name)

replace_phone / name / old_phone/ new_phone
replace_email / name /old_email/ new_email
replace_birthday / name /old_birthday/ new_birthday
replace_address / name /old_address/ address
delete_phone / name / old_phone
delete_email / name /old_email

add_note / name_note | description(optional) | tags (optional)
add_desc_to_note / name_note / description
add_tag_to_note / name_note / tagsort_notes (by tags)
search_note (by tags)
sort_func
quit"""

COMMANDS = {
    'hello': hello,
    'add' : add_new_contact,
    'delete' : delete,
    'add_phone' : add_phones,
    'add_email' : add_emails,
    'add_birthday' : add_birthdays,
    'add_address' :add_address,
    'replace_phone' : replace_phone,
    'replace_email' : replace_email,
    'replace_birthday' : replace_birthday,
    'replace_address' : replace_address,
    'delete_phone' : delete_phone,
    'delete_email' : delete_email,
    'find' : searcher,
    'quit' : quit}
# 'add_note' 
# 'add_desc_to_note' / name_note / description
# 'add_tag_to_note' / name_note / tagsort_notes (by tags)
# 'search_note' (by tags)
# 'sort_func'
# 'delete_birthday' : 
# 'delete_addres' / name /old_addres
# 'search_contact' / name
# 'replace_desc_of_note'
# 'search_note' (by name)
# 'delete_note' (by name)

addressbook = AddressBook()

@corrector
def answer_exit():
    return 'Good bye!'

@corrector
def command_error():
    return 'Wrong command, please try again.'

def get_answer_function(answer):
    return COMMANDS.get(answer, command_error)

# @corrector
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
