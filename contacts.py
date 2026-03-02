import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add_contact(name, phone):
    """Pievieno jaunu kontaktu."""
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"✓ Pievienots: {name} ({phone})")

def list_contacts():
    """Izvada visus ierakstītos kontaktus"""
    contacts = load_contacts()
    if not contacts:
        print("Kontakta saraksts ir tukšs!")
        return
    
    print("Kontakti: ")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact["name"]} - {contact["phone"]}")

def search_contacts(query):
    """Meklē kontaktus pēc vārda"""
    contacts = load_contacts()
    results = [contact for contact in contacts
               if query.lower() in contact["name"].lower()]
    
    if not results:
        print("Kontakts netika atrasts.")
        return
    
    print(f"Atrasti {len(results)} kontakti:")
    for index, contact in enumerate(results, start=1):
        print(f"{index}. {contact["name"]} - {contact["phone"]}")

def main():
    if len(sys.argv) < 2:
        print("Lietošana:")
        print("python contacts.py add \"Vārds\" \"Telefons\"")
        print("python contacts.py list")
        print("python contacts.py search Vārds")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Nepareizs argumentu skaits komandai add.")
            return
        add_contact(sys.argv[2], sys.argv[3])

    elif command == "list":
        list_contacts()

    elif command == "search":
        if len(sys.argv) != 3:
            print("Nepareizs argumentu skaits komandai search.")
            return
        search_contacts(sys.argv[2])

    else:
        print("Nezināma komanda.")

if __name__ == "__main__":
    main()

