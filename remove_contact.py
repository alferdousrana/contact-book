def remove_contact():
    phone_to_remove = input("Enter phone number to remove: ")
    
    try:
        with open("contacts.svg", "r") as file:
            contacts = file.read()
            contact_list = contacts.strip().split("\n\n")
            new_contacts = []
            contact_found = False

            for contact in contact_list:
                if f"Phone: {phone_to_remove}" in contact:
                    contact_found = True
                else:
                    new_contacts.append(contact)
            
            if contact_found:
                with open("contacts.svg", "w") as file:
                    file.write("\n\n".join(new_contacts) + "\n\n" if new_contacts else "")
                print("Your contact removed successfully.")
            else:
                print("No contact available for removal.")
    except FileNotFoundError:
        print("No contacts available.")
