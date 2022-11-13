"""replace_phone / name / old_phone/ new_phone
replace_email / name /old_email/ new_email
replace_birthday / name /old_birthday/ new_birthday
replace_address / name /old_addres/ addres
delete_phone / name / old_phone
delete_email / name /old_email"""

def replace_phone(data):
    data = data.strip().split()
    name = data[0]
    old_phone = data[1]
    new_phone = data[2]
    record = ADDRESSBOOK.data[name]
    record.change_phone(old_phone, new_phone)
    return f'In contact {name} successfully changed phone {old_phone} to {new_phone}'


def replace_email(data):
    data = data.strip().split()
    name = data[0]
    old_email = data[1]
    new_email = data[2]
    record = ADDRESSBOOK.data[name]
    record.change_phone(old_email, new_email)
    pass
    # return f'In contact {name} successfully changed email {old_email} to {new_email}'


def replace_birthday(data):
    data = data.strip().split()
    name = data[0]
    old_birthday = data[1]
    new_birthday = data[2]
    record = ADDRESSBOOK.data[name]
    record.change_phone(old_birthday, new_birthday)
    return f'In contact {name} successfully changed birth date {old_birthday} to {new_birthday}'
    

def replace_address(data):
    data = data.strip().split()
    name = data[0]
    old_address = data[1]
    new_address = data[2]
    record = ADDRESSBOOK.data[name]
    record.change_address(old_address, new_address)
    return f'In contact {name} successfully changed address {old_address} to {new_address}'
    

def delete_phone(data):
    data = data.strip().split()
    name = data[0]
    old_phone = data[1]
    record = ADDRESSBOOK.data[name]
    record.delete_phone(old_phone)
    return f'In contact {name} successfully deleted phone {old_phone}'


def delete_email(data):
    data = data.strip().split()
    name = data[0]
    old_email = data[1]
    record = ADDRESSBOOK.data[name]
    record.delete_email(old_email)
    # return f'In contact {name} successfully deleted email {old_email}'
    pass