def read_customer_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid number of arguments."
        except KeyError:
            return "Contact not found."

    return inner


@input_error
def add_contact_safely(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact_safely(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError("Contact not found.")


@input_error
def get_phone_safely(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found.")


def show_all_contacts(contacts):
    if not contacts:
        return "No contacts stored."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = read_customer_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact_safely(args, contacts))
        elif command == "change":
            print(change_contact_safely(args, contacts))
        elif command == "phone":
            print(get_phone_safely(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
