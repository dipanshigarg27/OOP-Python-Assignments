# ============================================================
# QUESTION 1: SMART PARKING MANAGEMENT SYSTEM
# ============================================================

# QUESTION:
# A smart parking facility wants to develop a Parking Management
# System to automatically calculate parking charges for different
# types of vehicles.
#
# The system supports three types of vehicles:
#   Car             -> ₹50 per hour
#   Bike            -> ₹20 per hour
#   Electric Vehicle -> ₹30 per hour
#
# Every vehicle has:
#   1. Vehicle Number
#   2. Owner Name
#   3. Number of Hours Parked
#
# The system should store and display the vehicle details and
# calculate the total parking charge based on the vehicle type
# and the number of hours parked.
#
# The program should create at least one object of Car, Bike,
# and Electric Vehicle and display their details along with
# their respective parking charges.
#
# NOTE:
# Every vehicle should follow a common structure for displaying
# its information, while the method for calculating the parking
# charge can be different for each type of vehicle.
#
# ============================================================
# CONCEPT USED:
# Inheritance and Method Overriding
# ============================================================


# ------------------------------------------------------------
# PARENT CLASS
# ------------------------------------------------------------
# Vehicle is the parent class.
#
# It contains the information that is common to all vehicles:
# vehicle number, owner name, and hours parked.
#
# The display() method is also common to all vehicles.
class Vehicle:

    # Constructor to initialize common vehicle information.
    def __init__(self, vehicle_number, owner_name, hours):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.hours = hours

    # This method displays the common information of a vehicle.
    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Owner Name:", self.owner_name)
        print("Hours Parked:", self.hours)


# ------------------------------------------------------------
# CHILD CLASS: CAR
# ------------------------------------------------------------
# Car inherits the properties and methods of Vehicle.
#
# The parking charge for a car is ₹50 per hour.
class Car(Vehicle):

    # This method calculates the parking charge for a car.
    #
    # The method is different from the other vehicle classes
    # because each vehicle type has a different parking rate.
    def calculate_charge(self):
        return self.hours * 50


# ------------------------------------------------------------
# CHILD CLASS: BIKE
# ------------------------------------------------------------
# Bike also inherits from the Vehicle class.
#
# The parking charge for a bike is ₹20 per hour.
class Bike(Vehicle):

    # This method calculates the parking charge for a bike.
    def calculate_charge(self):
        return self.hours * 20


# ------------------------------------------------------------
# CHILD CLASS: ELECTRIC VEHICLE
# ------------------------------------------------------------
# ElectricVehicle inherits from the Vehicle class.
#
# The parking charge for an electric vehicle is ₹30 per hour.
class ElectricVehicle(Vehicle):

    # This method calculates the parking charge for an
    # electric vehicle.
    def calculate_charge(self):
        return self.hours * 30


# ============================================================
# OBJECT CREATION
# ============================================================

# Creating an object of the Car class.
# Vehicle Number = HR01AB1234
# Owner Name = Rahul
# Hours Parked = 4
car1 = Car("HR01AB1234", "Rahul", 4)


# Creating an object of the Bike class.
# Vehicle Number = HR02CD5678
# Owner Name = Aman
# Hours Parked = 4
bike1 = Bike("HR02CD5678", "Aman", 4)


# Creating an object of the ElectricVehicle class.
# Vehicle Number = DL03EF9012
# Owner Name = Riya
# Hours Parked = 4
ev1 = ElectricVehicle("DL03EF9012", "Riya", 4)


# ============================================================
# DISPLAYING CAR DETAILS
# ============================================================

print("----- CAR DETAILS -----")

# display() is inherited from the Vehicle class.
car1.display()

# calculate_charge() is defined specifically for the Car class.
print("Parking Charge: ₹", car1.calculate_charge())

print()


# ============================================================
# DISPLAYING BIKE DETAILS
# ============================================================

print("----- BIKE DETAILS -----")

# display() is inherited from the Vehicle class.
bike1.display()

# calculate_charge() is defined specifically for the Bike class.
print("Parking Charge: ₹", bike1.calculate_charge())

print()


# ============================================================
# DISPLAYING ELECTRIC VEHICLE DETAILS
# ============================================================

print("----- ELECTRIC VEHICLE DETAILS -----")

# display() is inherited from the Vehicle class.
ev1.display()

# calculate_charge() is defined specifically for the
# ElectricVehicle class.
print("Parking Charge: ₹", ev1.calculate_charge())




