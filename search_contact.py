def search_contact():
    phone_to_search = input("Enter phone number to search: ")
    
    try:
        with open("contacts.svg", "r") as file:
            contacts = file.read()
            if phone_to_search in contacts:
                contact_list = contacts.split("\n\n")
                for contact in contact_list:
                    if f"Phone: {phone_to_search}" in contact:
                        print("\nContact Found:")
                        print(contact)
                        return
                print("No contact available.")
            else:
                print("No contact available.")
    except FileNotFoundError:
        print("No contacts available.")
