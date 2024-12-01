import os

def add_contact():
    try:
        name = input("Enter contact name: ")
        if not name.isalpha():
            raise ValueError("Name must be a string containing only alphabets.")

        phone = input("Enter phone number: ")
        if not phone.isdigit():
            raise ValueError("Phone number containing only digits.")

        email = input("Enter email: ")
        address = input("Enter address: ")

        if not os.path.exists("contacts.svg"):
            with open("contacts.svg", "w") as file:
                file.write("")

        with open("contacts.svg", "r") as file:
            contacts = file.readlines()
            for contact in contacts:
                if f"Phone: {phone}" in contact:
                    print("The number already exists.")
                    return

        with open("contacts.svg", "a") as file:
            file.write(f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}\n\n")

        print("A new contact added successfully.")
    except ValueError as e:
        print(e)
        add_contact()
