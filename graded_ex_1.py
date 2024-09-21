# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    while True:
        if sort_order == "1" or sort_order.lower() == "asc":: 
            sorted_products = sorted(products_list, key=lambda x: x[1], reverse=False)
            break
        elif sort_order == "2" or sort_order.lower() == "desc"::  
            sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
            break
        else:
            print("Invalid sort_order. Use '1' or '2'.")
            return None 
    return sorted_products

def display_products(products_list):
    for i, (product_name, price) in enumerate(products_list, start=1):
        print(f"{i}. {product_name}: ${price}")  


def display_categories():
    categories = list(products.keys())
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))  

def display_cart(cart):
    print("Your Cart:")
    if not cart:
        print("Your cart is empty.")
        return
    total_cost = 0
    for product_name, price, quantity in cart:
        item_total = price * quantity
        total_cost += item_total
        print(f"{product_name} - ${price} x {quantity} = ${item_total}")
    print(f"Total cost: ${total_cost}")




def generate_receipt(name, email, cart, total_cost, address):
    print("Receipt")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products Purchased:")
    for product_name, price, quantity in cart:
        item_total = price * quantity
        print(f"{product_name} (x{quantity}) - ${price} each = ${item_total}")
    print(f"Total Cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered.")



def validate_name(name):
    parts = name.split() 
    if len(parts) == 2 and all(part.isalpha() for part in parts):
        return True
    return False




def validate_email(email):
    if "@" in email:
        return True
    return False




def main():
    name = input("Enter your name (first and last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name (first and last): ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email.")
        email = input("Enter your email: ")
    cart = []
    total_cost = 0

    while True:
        print("\nAvailable Categories:")
        display_categories()
        
        category_choice = int(input("Select a category by number: "))
        while category_choice < 1 or category_choice > len(products):
            print("Invalid choice. Please try again.")
            category_choice = int(input("Select a category by number: "))

        selected_category = list(products.keys())[category_choice - 1]
        
        while True:
            print(f"\nProducts in {selected_category}:")
            display_products(products[selected_category])
            print("——————————————————————————————————————")
            print("Options:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
          
            
            option = int(input("Select an option by number: "))
            
            if option == 1:
                product_choice = int(input("Enter the product's number to buy: "))
                quantity = int(input("Enter the quantity you want: "))
                product = products[selected_category][product_choice - 1]
                add_to_cart(cart, product, quantity)
                total_cost += product[1] * quantity
            
            elif option == 2:
                sort_order = int(input("Sort by price (1: Ascending, 2: Descending): "))
                display_sorted_products(products[selected_category], sort_order)
            elif option == 3:
                break  
            elif option == 4:
                if cart:
                    display_cart(cart)
                    print(f"Total cost: ${total_cost}")
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return  

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()





# def display_sorted_products(products_list, sort_order):
#     sorted_list = sorted(products_list, key=lambda x: x[1], reverse=(0))
#     for product in sorted_list:
#         print(f"{product[0]} - price: {product[1]}")


# def display_products(products_list):
#     for product in products_list:
#         print(f"{product[0]} - price: {product[1]}")


# def display_categories():
#     category = input("Select a category (IT Products, Electronics, Groceries): ")
#     if category in products:
#         print("Sort by price: 1) Ascending 2) Descending")
#         sort_order = int(input("Enter your choice: "))
#         if sort_order in [1, 2]:
#             display_sorted_products(products[category], sort_order)
#         else:
#             print("Invalid option.")
#     else:
#         print("Category not found.")
 


