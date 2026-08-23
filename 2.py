# ============================================================
# QUESTION 2: FOOD DELIVERY MANAGEMENT SYSTEM
# ============================================================

# QUESTION:
# A food delivery platform wants to calculate delivery charges
# for different types of orders.
#
# The platform supports three delivery categories:
#
#   Standard Delivery -> ₹40 base charge + ₹10 per kilometer
#   Express Delivery  -> ₹80 base charge + ₹20 per kilometer
#   Premium Delivery  -> ₹120 base charge + ₹30 per kilometer
#
# Every delivery order contains:
#   1. Order ID
#   2. Customer Name
#   3. Restaurant Name
#   4. Distance in kilometers
#
# The system must display complete order details and calculate
# the final delivery charge according to the selected
# delivery category.
#
# The system should represent all three delivery categories
# using suitable objects.
#
# NOTE:
# Each delivery category should follow the same basic structure
# while having its own way of calculating the final delivery
# charge.
#
# ============================================================
# CONCEPT USED:
# Inheritance and Method Overriding
# ============================================================


# ------------------------------------------------------------
# PARENT CLASS
# ------------------------------------------------------------
# Delivery is the parent class.
#
# It contains the information that is common to all delivery
# categories:
# Order ID, Customer Name, Restaurant Name, and Distance.
#
# The display() method is also common to all categories.
class Delivery:

    # Constructor to initialize common order information.
    def __init__(self, order_id, customer_name, restaurant_name, distance):
        self.order_id = order_id
        self.customer_name = customer_name
        self.restaurant_name = restaurant_name
        self.distance = distance

    # This method displays the common details of the order.
    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Restaurant Name:", self.restaurant_name)
        print("Distance:", self.distance, "km")


# ------------------------------------------------------------
# CHILD CLASS: STANDARD DELIVERY
# ------------------------------------------------------------
# StandardDelivery inherits the properties and methods
# from the Delivery class.
#
# Standard Delivery:
# Base charge = ₹40
# Charge per kilometer = ₹10
class StandardDelivery(Delivery):

    # This method calculates the final delivery charge
    # for Standard Delivery.
    def calculate_charge(self):
        return 40 + (self.distance * 10)


# ------------------------------------------------------------
# CHILD CLASS: EXPRESS DELIVERY
# ------------------------------------------------------------
# ExpressDelivery inherits from the Delivery class.
#
# Express Delivery:
# Base charge = ₹80
# Charge per kilometer = ₹20
class ExpressDelivery(Delivery):

    # This method calculates the final delivery charge
    # for Express Delivery.
    def calculate_charge(self):
        return 80 + (self.distance * 20)


# ------------------------------------------------------------
# CHILD CLASS: PREMIUM DELIVERY
# ------------------------------------------------------------
# PremiumDelivery inherits from the Delivery class.
#
# Premium Delivery:
# Base charge = ₹120
# Charge per kilometer = ₹30
class PremiumDelivery(Delivery):

    # This method calculates the final delivery charge
    # for Premium Delivery.
    def calculate_charge(self):
        return 120 + (self.distance * 30)


# ============================================================
# OBJECT CREATION
# ============================================================

# Creating an object of StandardDelivery.
# Order ID = 101
# Customer Name = Rahul
# Restaurant Name = Domino's
# Distance = 5 km
standard1 = StandardDelivery(101, "Rahul", "Domino's", 5)


# Creating an object of ExpressDelivery.
# Order ID = 102
# Customer Name = Aman
# Restaurant Name = Pizza Hut
# Distance = 5 km
express1 = ExpressDelivery(102, "Aman", "Pizza Hut", 5)


# Creating an object of PremiumDelivery.
# Order ID = 103
# Customer Name = Riya
# Restaurant Name = Burger King
# Distance = 5 km
premium1 = PremiumDelivery(103, "Riya", "Burger King", 5)


# ============================================================
# DISPLAYING STANDARD DELIVERY DETAILS
# ============================================================

print("----- STANDARD DELIVERY -----")

# display() is inherited from the Delivery class.
standard1.display()

# calculate_charge() is defined specifically for
# StandardDelivery.
print("Final Delivery Charge: ₹", standard1.calculate_charge())

print()


# ============================================================
# DISPLAYING EXPRESS DELIVERY DETAILS
# ============================================================

print("----- EXPRESS DELIVERY -----")

# display() is inherited from the Delivery class.
express1.display()

# calculate_charge() is defined specifically for
# ExpressDelivery.
print("Final Delivery Charge: ₹", express1.calculate_charge())

print()


# ============================================================
# DISPLAYING PREMIUM DELIVERY DETAILS
# ============================================================

print("----- PREMIUM DELIVERY -----")

# display() is inherited from the Delivery class.
premium1.display()

# calculate_charge() is defined specifically for
# PremiumDelivery.
print("Final Delivery Charge: ₹", premium1.calculate_charge())

