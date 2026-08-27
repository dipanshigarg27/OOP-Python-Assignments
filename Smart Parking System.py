# Smart Parking System
#
# This program manages parking for Bikes, Cars and SUVs.
# It keeps track of parking slots, vehicle details,
# parking charges and lost ticket penalties.
#
# OOP concepts used:
# - Classes and Objects
# - Inheritance
# - Method Overriding
# - Polymorphism
# - Constructors


# Parent class
class Vehicle:

    def __init__(self, registration_number, owner_name, vip=False):
        self.registration_number = registration_number
        self.owner_name = owner_name
        self.vip = vip

    def calculate_fee(self, hours):
        return 0

    def get_lost_ticket_penalty(self):
        return 0

    def display_details(self):
        print("Registration Number:", self.registration_number)
        print("Owner Name:", self.owner_name)
        print("VIP Customer:", self.vip)


# Bike class
class Bike(Vehicle):

    def calculate_fee(self, hours):

        # ₹20 for the first hour and ₹10 for every
        # additional hour
        if hours <= 1:
            fee = 20
        else:
            fee = 20 + (hours - 1) * 10

        # Maximum charge per day is ₹100
        if fee > 100:
            fee = 100

        # VIP customers get 20% discount
        if self.vip:
            fee = fee * 0.80

        return fee

    def get_lost_ticket_penalty(self):
        return 200

    def display_details(self):
        print("\nVehicle Type: Bike")
        Vehicle.display_details(self)


# Car class
class Car(Vehicle):

    def calculate_fee(self, hours):

        # ₹50 for the first hour and ₹30 for every
        # additional hour
        if hours <= 1:
            fee = 50
        else:
            fee = 50 + (hours - 1) * 30

        # Maximum charge per day is ₹300
        if fee > 300:
            fee = 300

        # VIP customers get 20% discount
        if self.vip:
            fee = fee * 0.80

        return fee

    def get_lost_ticket_penalty(self):
        return 500

    def display_details(self):
        print("\nVehicle Type: Car")
        Vehicle.display_details(self)


# SUV class
class SUV(Vehicle):

    def calculate_fee(self, hours):

        # ₹80 for the first hour and ₹50 for every
        # additional hour
        if hours <= 1:
            fee = 80
        else:
            fee = 80 + (hours - 1) * 50

        # Maximum charge per day is ₹500
        if fee > 500:
            fee = 500

        # VIP customers get 20% discount
        if self.vip:
            fee = fee * 0.80

        return fee

    def get_lost_ticket_penalty(self):
        return 800

    def display_details(self):
        print("\nVehicle Type: SUV")
        Vehicle.display_details(self)


# Parking slot class
class ParkingSlot:

    def __init__(self, slot_number, vehicle_type, charging=False):
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.charging = charging
        self.occupied = False
        self.vehicle = None

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    def release_slot(self):
        self.vehicle = None
        self.occupied = False


# Parking system class
class ParkingSystem:

    def __init__(self):

        self.bike_slots = []
        self.car_slots = []
        self.suv_slots = []

        # Creating 50 bike slots
        for i in range(1, 51):
            self.bike_slots.append(ParkingSlot(i, "Bike"))

        # Creating 30 car slots
        for i in range(1, 31):
            self.car_slots.append(ParkingSlot(i, "Car"))

        # Creating 20 SUV slots
        for i in range(1, 21):
            self.suv_slots.append(ParkingSlot(i, "SUV"))

    def find_slot(self, vehicle):

        # The type of object decides which slots to check.
        # This avoids using if vehicle_type == "car" etc.

        if isinstance(vehicle, Bike):
            slots = self.bike_slots

        elif isinstance(vehicle, Car):
            slots = self.car_slots

        else:
            slots = self.suv_slots

        for slot in slots:
            if not slot.occupied:
                return slot

        return None

    def enter_vehicle(self, vehicle):

        slot = self.find_slot(vehicle)

        if slot is None:
            print("\nParking Full")
            return None

        slot.park_vehicle(vehicle)

        print("\nVehicle Entry Successful")
        print("Slot Number:", slot.slot_number)

        return slot

    def exit_vehicle(self, slot, hours):

        # The correct calculate_fee() method is called
        # depending on the vehicle object.
        fee = slot.vehicle.calculate_fee(hours)

        print("\nVehicle Exit")
        print("-------------------------")

        slot.vehicle.display_details()

        print("Parking Hours:", hours)
        print("Parking Fee: ₹", fee)

        slot.release_slot()

        print("Slot Released Successfully")

    def lost_ticket(self, slot):

        penalty = slot.vehicle.get_lost_ticket_penalty()

        print("\nLost Ticket")
        print("-------------------------")
        print("Registration Number:",
              slot.vehicle.registration_number)
        print("Penalty: ₹", penalty)

        slot.release_slot()

        print("Slot Released Successfully")


# Creating the parking system
parking = ParkingSystem()


# Creating vehicle objects
bike1 = Bike("DL01AB1234", "Rahul")

car1 = Car("DL02CD5678", "Aman", True)

suv1 = SUV("DL03EF9012", "Priya")


# Vehicles enter the parking
bike_slot = parking.enter_vehicle(bike1)
car_slot = parking.enter_vehicle(car1)
suv_slot = parking.enter_vehicle(suv1)


# Vehicles leave the parking

# Bike parked for 4 hours
if bike_slot:
    parking.exit_vehicle(bike_slot, 4)

# VIP car parked for 5 hours
if car_slot:
    parking.exit_vehicle(car_slot, 5)

# SUV parked for 6 hours
if suv_slot:
    parking.exit_vehicle(suv_slot, 6)


# Lost ticket example
car2 = Car("DL04GH3456", "Rohit")

lost_ticket_slot = parking.enter_vehicle(car2)

if lost_ticket_slot:
    parking.lost_ticket(lost_ticket_slot)
