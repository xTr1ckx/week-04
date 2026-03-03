import sys
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units

def add_item(name, qty, price):
    items = load_list()

    try:
        qty = int(qty)
        if qty <= 0:
            print("Daudzumam jābūt pozitīvam skaitlim!")
            return
    except ValueError:
        print("Daudzumam jābūt veselam skaitlim!")
        return
    
    try:
        price = float(price)
        if price < 0:
            print("Cena nedrīkst būt negatīva!")
            return
    except ValueError:
        print("Cenai ir jābūt skaitlim!")
        return
    
    item = {"name": name, "qty": qty, "price": price}

    items.append(item)
    save_list(items)

    line_total = calc_line_total(item)

    print(f"✓ Pievienots: {name} x {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

def list_items():
    items = load_list()

    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    
    print("Iepirkumu saraksts:")

    for index, item in enumerate(items, start=1):
        line_total = calc_line_total(item)
        print(f"{index}. {item["name"]} x {item["qty"]} - "
              f"{item["price"]:.2f} EUR/gab. - {line_total:.2f} EUR")

def calculate_total():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs.")
        return
    
    grand_total = calc_grand_total(items)
    product_count = len(items)
    unit_count = count_units(items)

    #total = sum(item["price"] for item in items)
    #count = len(items)

    #print(f"Kopā: {total:.2f} EUR ({count} produkti)")

    print(f"Kopā: {grand_total:.2f} EUR ({unit_count} vienības, {product_count} produkti.)")

def clear_list():
    save_list([])
    print("✓ Saraksts notīrīts.")

def main():
    if len(sys.argv) < 2:
        print("Lietošana:")
        print("python shop.py add Nosaukums Daudzums Cena")
        print("python shop.py list")
        print("python shop.py total")
        print("python shop.py clear")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 5:
            print("Nepareizs argumentu skaits komandai add (python shop.py add Nosaukums Daudzums Cena).")
            return
        add_item(sys.argv[2], sys.argv[3], sys.argv[4])

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