# ============================================================
# QUESTION 3: E-COMMERCE SHIPPING MANAGEMENT SYSTEM
# ============================================================

# QUESTION:
# An e-commerce company wants to calculate shipping charges
# for different categories of packages.
#
# The company uses the following pricing rules:
#
#   Regular Package -> ₹50 + ₹15 per kg
#   Fragile Package -> ₹100 + ₹25 per kg
#   Express Package -> ₹150 + ₹40 per kg
#
# Every package contains:
#   1. Package ID
#   2. Customer Name
#   3. Destination
#   4. Package Weight in kilograms
#
# The system must display package information and calculate
# the final shipping charge according to the package category.
#
# The system should represent all three package categories
# using suitable objects.
#
# NOTE:
# The system should maintain a common structure for package
# information while allowing each category to apply its own
# shipping-charge calculation.
#
# ============================================================
# CONCEPT USED:
# Inheritance and Method Overriding
# ============================================================


# ------------------------------------------------------------
# PARENT CLASS
# ------------------------------------------------------------
# Package is the parent class.
#
# It contains the information that is common to all packages:
# Package ID, Customer Name, Destination, and Weight.
#
# The display() method is also common to all package types.
class Package:

    # Constructor to initialize common package information.
    def __init__(self, package_id, customer_name, destination, weight):
        self.package_id = package_id
        self.customer_name = customer_name
        self.destination = destination
        self.weight = weight

    # This method displays the common package information.
    def display(self):
        print("Package ID:", self.package_id)
        print("Customer Name:", self.customer_name)
        print("Destination:", self.destination)
        print("Package Weight:", self.weight, "kg")


# ------------------------------------------------------------
# CHILD CLASS: REGULAR PACKAGE
# ------------------------------------------------------------
# RegularPackage inherits the properties and methods
# from the Package class.
#
# Regular Package:
# Base charge = ₹50
# Charge per kg = ₹15
class RegularPackage(Package):

    # This method calculates the shipping charge
    # for a Regular Package.
    def calculate_charge(self):
        return 50 + (self.weight * 15)


# ------------------------------------------------------------
# CHILD CLASS: FRAGILE PACKAGE
# ------------------------------------------------------------
# FragilePackage inherits from the Package class.
#
# Fragile Package:
# Base charge = ₹100
# Charge per kg = ₹25
class FragilePackage(Package):

    # This method calculates the shipping charge
    # for a Fragile Package.
    def calculate_charge(self):
        return 100 + (self.weight * 25)


# ------------------------------------------------------------
# CHILD CLASS: EXPRESS PACKAGE
# ------------------------------------------------------------
# ExpressPackage inherits from the Package class.
#
# Express Package:
# Base charge = ₹150
# Charge per kg = ₹40
class ExpressPackage(Package):

    # This method calculates the shipping charge
    # for an Express Package.
    def calculate_charge(self):
        return 150 + (self.weight * 40)


# ============================================================
# OBJECT CREATION
# ============================================================

# Creating an object of RegularPackage.
# Package ID = 101
# Customer Name = Rahul
# Destination = Delhi
# Weight = 5 kg
regular1 = RegularPackage(101, "Rahul", "Delhi", 5)


# Creating an object of FragilePackage.
# Package ID = 102
# Customer Name = Aman
# Destination = Mumbai
# Weight = 5 kg
fragile1 = FragilePackage(102, "Aman", "Mumbai", 5)


# Creating an object of ExpressPackage.
# Package ID = 103
# Customer Name = Riya
# Destination = Bangalore
# Weight = 5 kg
express1 = ExpressPackage(103, "Riya", "Bangalore", 5)


# ============================================================
# DISPLAYING REGULAR PACKAGE DETAILS
# ============================================================

print("----- REGULAR PACKAGE -----")

# display() is inherited from the Package class.
regular1.display()

# calculate_charge() is defined specifically for
# RegularPackage.
print("Final Shipping Charge: ₹", regular1.calculate_charge())

print()


# ============================================================
# DISPLAYING FRAGILE PACKAGE DETAILS
# ============================================================

print("----- FRAGILE PACKAGE -----")

# display() is inherited from the Package class.
fragile1.display()

# calculate_charge() is defined specifically for
# FragilePackage.
print("Final Shipping Charge: ₹", fragile1.calculate_charge())

print()


# ============================================================
# DISPLAYING EXPRESS PACKAGE DETAILS
# ============================================================

print("----- EXPRESS PACKAGE -----")

# display() is inherited from the Package class.
express1.display()

# calculate_charge() is defined specifically for
# ExpressPackage.
print("Final Shipping Charge: ₹", express1.calculate_charge())