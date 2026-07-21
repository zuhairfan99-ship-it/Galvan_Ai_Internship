# Contact Management System
import json
def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    print(f"Contact for '{name}' added successfully!")
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, 1):
        print(
            f"{i}. Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )
def search_contact(contacts):
    search_term = input("Enter name to search: ").strip().lower()
    results = [
        contact for contact in contacts
        if search_term in contact["name"].lower()
    ]
    if not results:
        print("No matching contacts found.")
        return
    print("\n--- Search Results ---")
    for contact in results:
        print(
            f"Name: {contact['name']} | "
            f"Phone: {contact['phone']} | "
            f"Email: {contact['email']}"
        )
def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Contact '{removed['name']}' deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Saving contacts and exiting...")
            save_contacts(contacts)
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
if __name__ == "__main__":
    main()