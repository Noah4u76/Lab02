# Name: Noah Sanderson
# Date: 9/5/2024
# Purpose of File: Add, modify, delete contacts in list.

def print_list(contacts):
    """
    Printing a list of contacts with first name, last name and index.
    """
    print("================= CONTACT LIST ==================")
    print(f'{"Index":<8}{"First Name":<22}{"Last Name":<22}')
    print(f'{"======":<8}{"====================":<22}{"====================":<22}')
    for i in range(len(contacts)):
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
        
def add_contact(contacts):
    """
    Adding new contacts to the list
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    contacts.append([first_name,last_name])
    
    return contacts

def modify_contact(contacts):
    """
    Prompt the user for the list index number to modify.
    """
    index = int(input("Enter the index number of contact to modify: "))
    
    if 0<= index < len(contacts):
        first_name = input("Enter new first name: ")
        last_name = input("Enter new last name: ")
        
        contacts[index] = [first_name, last_name]
        
        return contacts
    else:
        print("Invalid index number.")
        return contacts
    
def delete_contact(contacts):
        """
        Delete contact from list.
        """
        index = int(input("Enter the index number of the contact to delete:"))
        if 0<= index < len(contacts):
            del contacts[index]
            return contacts
        else:
            print("Invalid index number")
            return contacts