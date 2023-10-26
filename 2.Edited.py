from collections import UserDict


class Field:
    """Базовий клас для полів запису."""

    def __init__(self, value):
        self.value = value


class Name(Field):
    """Клас для зберігання імені контакту. Обов'язкове поле."""

    pass


class Phone(Field):
    """Клас для зберігання номера телефону. Має валідацію формату (10 цифр)."""

    def __init__(self, phone):
        if self.validate(phone):
            super().__init__(phone)
        else:
            raise ValueError("Invalid phone format")

    @staticmethod
    def validate(phone):
        return len(phone) == 10 and phone.isdigit()


class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів."""

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
    """Клас для зберігання та управління записами."""

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
