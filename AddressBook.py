from collections import UserDict
from Record import Record


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
