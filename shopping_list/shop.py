import sys
from storage import load_list, save_list, get_price, set_price
from utils import calc_line_total, calc_grand_total, count_units

def validate_qty(qty):
    try:
        qty = int(qty)
        if qty <= 0:
            print("Daudzumam jābūt pozitīvam skaitlim!")
            return None
        return qty
    except ValueError:
        print("Daudzumam jābūt veselam skaitlim!")
        return None
    
def validate_price(price_input):
    try:
        price = float(price_input)
        if price <= 0:
            print("Cenai jābūt pozitiīvam skaitlim!")
            return None
        return price
    except ValueError:
        print("Cenai jābūt skaitlim!")
        return None

def add_item(name, qty_input):
    qty = validate_qty(qty_input)
    if qty is None:
        return

    existing_price = get_price(name)

    if existing_price is not None:
        print(f"Atrasta cena: {existing_price:.2f} EUR/gab.")
        choice = input("[A]kceptēt / [M]ainīt? > ").strip().lower()

        if choice == "a":
            price = existing_price

        elif choice == "m":
            new_price_input = input("Jaunā cena: > ")
            price = validate_price(new_price_input)
            if price is None:
                return
            
            set_price(name, price)
            print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")
            
        else:
            print("Nepareiza izvēle (A / M).")
            return
        
    else:
        print("Cena nav zināma.")
        price_input = input("Ievadi cenu: > ")
        price = validate_price(price_input)
        if price is None:
            return
        
        set_price(name, price)
        print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")

    items = load_list()

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

    print(f"Kopā: {grand_total:.2f} EUR ({unit_count} vienības, {product_count} produkti.)")

def clear_list():
    save_list([])
    print("✓ Saraksts notīrīts.")

def main():
    if len(sys.argv) < 2:
        print("Lietošana:")
        print("python shop.py add Nosaukums Daudzums")
        print("python shop.py list")
        print("python shop.py total")
        print("python shop.py clear")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Nepareizs argumentu skaits komandai add (python shop.py add Nosaukums Daudzums Cena).")
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