# Function to calculate total cart price
def calculate_total(cart_items):
    # If cart is empty
    if not cart_items:
        return "Cart is empty"
    # Calculate total price of items
    total = sum(cart_items.values())
    # Apply 10% discount if more than 5 items
    if len(cart_items) > 5:
        total *= 0.9
    # Return final total
    return f"Total price:{int(total)}"
# Dictionary to store items and prices
cart_items = {}
# Take number of items from user
n = int(input("Enter number of items: "))
for _ in range(n):
    item = input("Enter item name: ")
    price = float(input(f"Enter price for {item}: "))
    cart_items[item] = price  
# Print the total cart price
print(calculate_total(cart_items))
