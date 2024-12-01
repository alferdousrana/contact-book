def view_contacts():
    try:
        with open("contacts.svg", "r") as file:
            contacts = file.read()
            if contacts.strip() == "":
                print("No contacts available.")
            else:
                print("Contacts:\n")
                print(contacts)
    except FileNotFoundError:
        print("No contacts available.")
