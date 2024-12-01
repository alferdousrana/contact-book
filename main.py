from add_contact import add_contact
from view_contacts import view_contacts
from search_contact import search_contact
from remove_contact import remove_contact

def main():
    while True:
        print("\nContact Book Management System")
        print("0 - Exit")
        print("1 - Add Contact")
        print("2 - View Contacts")
        print("3 - Search Contact")
        print("4 - Remove Contact")
        
        choice = input("Enter your choice: ")
        
        if choice == "0":
            print("Thank you for using the Contact Book Management System. Goodbye!")
            break
        elif choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            remove_contact()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
