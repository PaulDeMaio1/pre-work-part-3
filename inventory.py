inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "speaker": {"price": 59.99, "quantity": 75},
    "monitor": {"price": 399.99, "quantity": 25},
}

LOW_STOCK_LIMIT = 10

def show_inventory():
    print("=" * 52)
    print(f"{'Item':<15}{'Price':>12}{'Qty':>10}{'Total':>14}")
    print("=" * 52)

    for name, info in inventory.items():
        total = info["price"] * info["quantity"]
        print(f"{name.title():<15}   ${info['price']:>9.2f}{info['quantity']:>8}   ${total:>11,.2f}")

    print("=" * 52)

    inventory_total = sum(info["price"] * info["quantity"] for info in inventory.values())
    print(f"{'Total inventory value:':<36}   ${inventory_total:>11,.2f}")
    print("=" * 52)

    low_stock = {name for name, info in inventory.items() if info["quantity"] < LOW_STOCK_LIMIT}

    if low_stock:
        names = ", ".join(name.title() for name in sorted(low_stock))
        print(f"Low Stock: {names}")
    else:
        print("All products are sufficiently stocked.")


show_inventory()

search = input("\nLook up a product: ").strip().lower()
product = inventory.get(search)

if product:
    print(f"\nProduct: {search.title()}")
    print(f"Price: ${product['price']:,.2f}")
    print(f"Quantity: {product['quantity']}")
    print(f"Total value: ${product['price'] * product['quantity']:,.2f}")

    print("\nWhat would you like to do?")
    print("1. Document a sale (remove stock)")
    print("2. Restock")
    print("3. Do nothing")
    choice = input("\nChoice: ").strip()

    if choice in ("1", "2"):
        try:
            amount = int(input("How many units? "))
            if amount <= 0:
                print("\nPlease enter a number greater than 0.")
            elif choice == "1" and amount > product["quantity"]:
                print(f"\nNot enough stock. Only {product['quantity']} in stock.")
            else:
                if choice == "1":
                    product["quantity"] -= amount
                    print(f"\nSold {amount} {search}(s).")
                else:
                    product["quantity"] += amount
                    print(f"\nRestocked {amount} {search}(s).")

                print("\nUpdated inventory:")
                show_inventory()
        except ValueError:
            print("\nPlease enter a valid whole number.")
    elif choice != "3":
        print("\nPlease enter 1, 2, or 3.")
else:
    print(f"\nNo product found for '{search}'.")