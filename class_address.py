from re import search


class Address:
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
            raise ValueError(f"Phone number {clean_address} is not valid")
        return str(value)
