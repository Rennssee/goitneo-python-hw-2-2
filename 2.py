class Phone(Field):
    def __init__(self, phone):
        if self.validate(phone):
            self.value = phone
        else:
            raise ValueError("Invalid phone format")

    @staticmethod
    def validate(phone):
        if len(phone) == 10 and phone.isdigit():
            return True
        return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        p = Phone(phone)
        self.phones.append(p)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
