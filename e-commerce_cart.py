def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty"
    total=sum(cart_items.values())
    if len(cart_items)>5:
        total*=0.9
    return f"Total price:{int(total)}"
cart_items = {}
n = int(input("Enter number of items: "))
for _ in range(n):
    item = input("Enter item name: ")
    price = float(input(f"Enter price for {item}: "))
    cart_items[item] = price
print(calculate_total(cart_items))