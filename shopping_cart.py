class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"): 
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        total_items = self.get_num_items_in_cart()
        print(f"Number of Items: {total_items}")

        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: Description placeholder")

def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n")

        if choice == "a":
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description:\n")  # Description is not used in the current class
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.add_item(new_item)

        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)

        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase(item_name, 0, new_quantity)
            cart.modify_item(modified_item)

        elif choice == "i":
            cart.print_descriptions()

        elif choice == "o":
            cart.print_total()

        elif choice == "q":
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)
