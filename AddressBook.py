from collections import UserDict
from Record import Record
from Note import Note


class AddressBook(UserDict):

    def __init__(self, data = None):
        super().__init__(data)
        self.notes = []

    def add_record(self, record):
        self.data[record.name.value] = record

    def return_record_by_name(self, name):
        return self.data[name]

    def remove_record(self, record):
        del self.data[record.name.value]

    def add_note(self, note):
        self.notes.append(Note(note))

    def remove_note(self, number_note):
        self.notes.pop(number_note)
