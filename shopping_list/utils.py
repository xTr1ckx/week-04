def calc_line_total(item):
    """Aprēķina vienas rindas summu (qty x price)."""
    return item["qty"] * item["price"]
    
def calc_grand_total(items):
    """Aprēķina kopējo summu visiem produktiem."""
    return sum(calc_line_total(item) for item in items)

def count_units(items):
    """Saskaita kopējo vienību skaitu."""
    return sum(item["qty"] for item in items)