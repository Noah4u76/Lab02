# Name: Noah Sanderson
# Date: 9/5/2024
# Purpose of file: Importing contacts.py

import contacts

def main():
    contact_list = []
    
    while True:
        print("/nMenu")
        print("1. Print list")
        print("2. Add contact")
        print("3. Modify contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            contacts.print_list(contact_list)
        elif choice == "2":
            contact_list = contacts.add_contact(contact_list)
        elif choice == "3":
            contact_list = contacts.modify_contact(contact_list)
        elif choice == "4":
                contact_list = contacts.delete_contact(contact_list)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number 1-5.")
            
if __name__ == "__main__":
    main()
