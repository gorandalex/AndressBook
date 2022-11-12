from Field import Field

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
        self.__value = value
