#Global dictionary to store contacts 
contacts = {}

def display_menu():
    
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. List All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    
    name = input("Enter contact name: ").strip().title() 
    
    
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        confirm = input("Do you want to update their details? (yes/no): ").lower()
        if confirm != 'yes':
            print("Contact not added/updated.")
            return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added/updated successfully.")

def view_contact():
    
    name = input("Enter contact name to view: ").strip().title()
    
    if name in contacts: 
        details = contacts[name]
        print(f"\n--- Details for {name} ---")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"Contact '{name}' not found.")

def list_all_contacts():
    
    if not contacts: 
        print("No contacts available.")
        return
    
    print("\n--- All Contacts ---")
    
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print("--------------------")

def delete_contact():
    
    name = input("Enter contact name to delete: ").strip().title()
    
    if name in contacts: 
        del contacts[name] 
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    #main app loop
    while True:
        display_menu() 
        choice = input("Enter choice (1-5): ")
        
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            list_all_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    
    main()