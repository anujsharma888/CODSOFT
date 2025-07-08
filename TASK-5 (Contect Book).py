contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email ID: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
        }
    contacts.append(contact)
    print("Contact added successfully.\n")

def view_contacts():
    if not contacts:
        print("Not exist.\n")
    else:
        for idx, c in enumerate(contacts, 1):
            print(f"{idx}. {c['name']} - {c['phone']}")
        print()

def search_contact():
    query = input("name or phone: ").lower()
    found = False
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\n")
            found = True
    if not found:
        print("contact not found.\n")

def update_contact():
    query = input("For update Enter name or phone number: ").lower()
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            print("Leave field blank to keep current value.")
            name = input(f"New name (current: {c['name']}): ") or c['name']
            phone = input(f"New phone (current: {c['phone']}): ") or c['phone']
            email = input(f"New email (current: {c['email']}): ") or c['email']
            address = input(f"New address (current: {c['address']}): ") or c['address']
            c.update({"name": name, "phone": phone, "email": email, "address": address})
            print("Contact Saved.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    query = input("Enter name or phone to delete: ").lower()
    for c in contacts:
        if query in c['name'].lower() or query in c['phone']:
            contacts.remove(c)
            print("Contact deleted .\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact ")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting...!")
            break
        else:
            print("Invalid choice.try again.\n")

menu()