# ============================================================
# LAB 7 - MY OWN ORDERING APP
# Week 7 - Hack the Hood
# ============================================================

# Name: Victoria Gano
#
# My store sells: Chips and Drinks

# ============================================================
# DAY 1 - BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint

class Chip:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 3: The price guard
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be below zero.")
        else:
            self.price = amount

    # TICKET 5: Each item's own action
    def serve(self):
        print("Opening your bag of chips!")


# TICKET 4: A second kind of item

class Drink(Chip):
    def serve(self):
        print("Pouring your cold drink!")


# TICKET 5 EXPLAIN:
# The same method name can do two different things because
# each class has its own version of serve().

# TICKET 2: Make your real items

# PREDICT:
# print(item1.name) will show: Spicy Chips

item1 = Chip("Spicy Chips", 3.50)
item2 = Drink("Lemonade", 2.50)

print(item1.name)


# TICKET 3: Test the price guard

# PREDICT:
# It will print "Price cannot be below zero."

item1.set_price(-5)

# Paste the message you see here:
# Price cannot be below zero.


# ============================================================
# DAY 2 - BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    # TICKET 9: Checkout
    def checkout(self):
        total = 0

        for item in self.items:
            item.serve()
            total += item.price

        print(f"Total: ${total:.2f}")


# TICKET 7: My menu and my cart

store = {
    "1": item1,
    "2": item2
}

cart = Cart()

print("\nWelcome to my Snack Shop!")
print("1. Spicy Chips - $3.50")
print("2. Lemonade - $2.50")


# TICKET 8: Let customers shop

# PREDICT:
# If I choose 1, Spicy Chips will be added to my cart.

while True:
    choice = input("Pick 1, 2, or 'done': ")

    if choice == "done":
        break
    elif choice in store:
        cart.add(store[choice])
        print(store[choice].name + " added!")
    else:
        print("Invalid choice.")


# TICKET 10: Test the whole app

# PREDICT:
# If I pick 1 and 2, then type done,
# both items will be added to my cart,
# each item will do its own action,
# and the total will be $6.00.

cart.checkout()