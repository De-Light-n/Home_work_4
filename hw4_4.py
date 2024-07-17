def show_all(contacts:dict):
    output = ""
    if contacts:
        for name, phone in contacts.items():
            output += f"{name} : {phone}\n"
        return output
    else:
        return "There is not any contscts\n"
        
def show_phone(args, contacts:dict):
    output = contacts.get(args[0])
    if output != None:
        return output
    else:
        return "Contact not founded"
        
def change_contact(args, contacts:dict):
    contacts[args[0]] = args[1]
    return "Contact changed"

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts), end="")       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
