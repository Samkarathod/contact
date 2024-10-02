contacts = []

def add_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)

def view_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact(name_or_phone):
    for contact in contacts:
        if contact['name'] == name_or_phone or contact['phone'] == name_or_phone:
            return contact
    return "Contact not found!"

# Adding a few contacts
add_contact("Alice", "1234567890", "alice@example.com", "123 Maple Street")
add_contact("Bob", "0987654321", "bob@example.com", "456 Oak Avenue")

# Viewing contacts
print("All Contacts:")
view_contacts()

# Searching for a contact
search_query = input("Enter name or phone number to search: ")
print(search_contact(search_query))