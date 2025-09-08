def add_menu(menu,item):
    menu.append(item)
    return menu
def remove_menu(menu,item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found")
    return menu
def check_item(menu,item):
    if item in menu:
        return f"{item} is available in menu"
    else:
        return f"{item} not available in menu"
menu = ["Pizza", "Burger", "Pasta", "Salad"]
while True:
    print("\nCurrent Menu:", menu)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Check Item")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice=="1":
        item=input("Enter item to add ")
        add_menu(menu,item)
    elif choice=="2":
        item=input("Enter item to remove ")
        remove_menu(menu,item)
    elif choice=="3":
        item=input("Enter item to check ")
        check_item(menu,item)
        print(check_item(menu, item))
    elif choice=="4":
        print("Final Menu ",menu)
        break
    else:
        print("Invalid choice ")

