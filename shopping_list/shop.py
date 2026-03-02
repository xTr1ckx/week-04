import sys
from storage import load_list, save_list

def add_item(name, price):
    items = load_list()

    try:
        price = float(price)
    except ValueError:
        print("Cenai ir jābūt skaitlim!")
        return
    
    items.append({"name": name, "price": price})
    save_list(items)

    print(f"✓ Pievienots: {name} ({price:.2f} EUR)")

def list_items():
    items = load_list()

    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    
    print("Iepirkumu saraksts:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item["name"]} - {item["price"]:.2f} EUR")

def calculate_total():
    items = load_list()

    total = sum(item["price"] for item in items)
    count = len(items)

    print(f"Kopā: {total:.2f} EUR ({count} produkti)")

def clear_list():
    save_list([])
    print("✓ Saraksts notīrīts.")

def main():
    if len(sys.argv) < 2:
        print("Lietošana:")
        print("python shop.py add Nosaukums Cena")
        print("python shop.py list")
        print("python shop.py total")
        print("python shop.py clear")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Nepareizs argumentu skaits komandai add.")
            return
        add_item(sys.argv[2], sys.argv[3])

    elif command == "list":
        list_items()

    elif command == "total":
        calculate_total()

    elif command == "clear":
        clear_list()

    else:
        print("Nezināma komanda.")

if __name__ == "__main__":
    main()