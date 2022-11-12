import Field
import re


class Phone(Field):

    @Field.value.setter
    def value(self, value:str):
        if not all((value.startswith('+380'), len(value) == 13, value[1:].isdigit())):
            raise ValueError("""Phone number {value} is not valid, 
            please enter correcct phone '+380XXXXXXX'""")
        self.__value = value


class Email(Field):
    
    @Field.value.setter
    def value(self, value:str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, value)):
            raise ValueError(""""Email {value} is not valid,
            please enter correct email.
            Example of emails: my.ownsite@our-earth.org
                                ankitrai326@gmail.com""")
        self.__value = value
