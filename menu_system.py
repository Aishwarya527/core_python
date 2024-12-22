def adding_item(menu,item):
    menu.append(item)
    print(f"Adding {item} to menu")
def remove_item(menu,item):
    if item in menu:
        menu.remove(item)
        print(f"{item} removed from menu")
    else:
        print(f"{item} not present in menu")
def check_item(menu,item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
print(f"initial menu:{initial_menu}")
adding_item(initial_menu,"Tacos")
remove_item(initial_menu,"Salad")
check_result = check_item(initial_menu,"Pizza" )
print(f"updated menu: {initial_menu}")
print(f"checking menu: {check_result}")

