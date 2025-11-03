
# ================================
# Shoe Inventory Management System
# ================================
# This program reads shoe data from a file (inventory.txt)
# and allows you to view, add, search, restock, and calculate
# values for each item in your shoe inventory.

import os

# Automatically find the folder where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the inventory file
inventory_file = os.path.join(base_dir, "inventory.txt")


# --------------------------------
# 1. Define the Shoe class
# --------------------------------
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        """Initialize a new Shoe object with given attributes."""
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)        # Convert to number
        self.quantity = int(quantity)  # Convert to number

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Return a readable string of the shoe's info."""
        return (f"{self.country} | {self.code} | {self.product} | "
                f"Cost: {self.cost} | Quantity: {self.quantity}")


# --------------------------------
# 2. List to store all shoes
# --------------------------------
shoes_list = []


# --------------------------------
# 3. Read shoes data from file
# --------------------------------
def read_shoes_data():
    """Read shoe data from the inventory.txt file and add to list."""
    try:
        with open(inventory_file, "r") as file:
            next(file)  # Skip the first header line
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    country, code, product, cost, quantity = parts
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoes_list.append(shoe)

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("""File not found. Please make sure 'inventory.txt'
                 is in this folder.""")
    except Exception as e:
        print("An error occurred while reading the file:", e)


# --------------------------------
# 4. Capture new shoe data
# --------------------------------
def capture_shoes():
    """Allow the user to enter a new shoe's data."""
    print("\nEnter new shoe details:")
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product name: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)
    print("Shoe added successfully!")


# --------------------------------
# 5. View all shoes
# --------------------------------
def view_all():
    """Display all shoes in the inventory."""
    if not shoes_list:
        print("No shoes in the list yet.")
        return

    print("\n--- All Shoes in Inventory ---")
    for shoe in shoes_list:
        print(shoe)


# --------------------------------
# 6. Restock the lowest quantity item
# --------------------------------
def re_stock():
    """Find the shoe with the lowest quantity and restock it."""
    if not shoes_list:
        print("No shoes loaded yet.")
        return

    lowest_shoe = min(shoes_list, key=lambda s: s.quantity)
    print(f"\nLowest stock item:\n{lowest_shoe}")

    choice = input("Would you like to restock this item? (yes/no): ").lower()
    if choice == "yes":
        try:
            add_qty = int(input("Enter quantity to add: "))
            lowest_shoe.quantity += add_qty
            print("Quantity updated!")
            update_inventory_file()
        except ValueError:
            print("Please enter a valid number.")


# --------------------------------
# 7. Search for a shoe by code
# --------------------------------
def search_shoe():
    """Search for a shoe by its code."""
    code = input("Enter shoe code to search: ").strip()

    for shoe in shoes_list:
        if shoe.code.lower() == code.lower():
            print("Shoe found:")
            print(shoe)
            return
    print("Shoe not found.")


# --------------------------------
# 8. Calculate total value per shoe
# --------------------------------
def value_per_item():
    """Calculate and print total value for each shoe."""
    if not shoes_list:
        print("No shoes loaded yet.")
        return

    print("\n--- Total Value per Shoe ---")
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) - Total Value: {value}")


# --------------------------------
# 9. Find shoe with the highest quantity
# --------------------------------
def highest_qty():
    """Display the shoe with the highest quantity."""
    if not shoes_list:
        print("No shoes loaded yet.")
        return

    highest_shoe = max(shoes_list, key=lambda s: s.quantity)
    print(f"\nHighest stock item (for sale!):\n{highest_shoe}")


# --------------------------------
# 10. Update inventory.txt after changes
# --------------------------------
def update_inventory_file():
    """Rewrite the inventory.txt file with updated data."""
    with open(inventory_file, "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoes_list:
            file.write(f"""{shoe.country},{shoe.code},
                           {shoe.product},{shoe.cost},
                           {shoe.quantity}\n""")


# --------------------------------
# 11. Main Menu
# --------------------------------
def main():
    """Main menu loop."""
    while True:
        print("\n====== SHOE INVENTORY MENU ======")
        print("1 - Read data from file")
        print("2 - View all shoes")
        print("3 - Add new shoe")
        print("4 - Restock lowest item")
        print("5 - Search by code")
        print("6 - Show value per item")
        print("7 - Show highest stock shoe")
        print("0 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            view_all()
        elif choice == "3":
            capture_shoes()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# --------------------------------
# 12. Run the program
# --------------------------------
if __name__ == "__main__":
    main()
