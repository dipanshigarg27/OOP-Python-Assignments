# Question 2
# Payment Gateway
#
# Create a payment system for an e-commerce application.
# The system supports UPI, Credit Card, Debit Card, Wallet
# and Net Banking.
#
# Each payment method has different transaction charges
# and transaction limits.
#
# The payment system should calculate the payment fee,
# cashback (if applicable) and final cost.
#
# The balance information should be kept confidential.
# Use abstraction for this purpose.


from abc import ABC, abstractmethod


# This is the common parent class for all payment methods.
# It contains the basic structure which every payment method follows.

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def payment(self):
        pass


# UPI payment method

class UPI(Payment):

    def payment(self):
        if self.amount > 100000:
            return "UPI transaction limit exceeded"

        fee = self.amount * 0.01

        if self.amount <= 100000:
            return f"Payment Fee: ₹{fee}"


# Credit Card payment method

class CreditCard(Payment):

    def payment(self):
        if self.amount > 200000:
            return "Credit Card transaction limit exceeded"

        fee = self.amount * 0.02
        cashback = 0

        if self.amount > 5000:
            cashback = self.amount * 0.01

        final_cost = self.amount + fee - cashback

        return f"Payment Fee: ₹{fee}, Cashback: ₹{cashback}, Final Cost: ₹{final_cost}"


# Debit Card payment method

class DebitCard(Payment):

    def payment(self):
        if self.amount > 100000:
            return "Debit Card transaction limit exceeded"

        fee = self.amount * 0.015

        return f"Payment Fee: ₹{fee}"


# Wallet payment method

class Wallet(Payment):

    def __init__(self, amount, balance):
        self.amount = amount

        # Balance is kept private so that it cannot be accessed
        # directly from outside the class.
        self.__balance = balance

    def payment(self):

        if self.amount > 50000:
            return "Wallet transaction limit exceeded"

        if self.amount > self.__balance:
            return "Insufficient Wallet Balance"

        fee = self.amount * 0.005

        return f"Payment Fee: ₹{fee}"


# Net Banking payment method

class NetBanking(Payment):

    def payment(self):

        if self.amount > 500000:
            return "Net Banking transaction limit exceeded"

        fee = 10

        return f"Payment Fee: ₹{fee}"


# Creating objects for different payment methods

upi = UPI(10000)
credit_card = CreditCard(10000)
debit_card = DebitCard(10000)
wallet = Wallet(10000, 20000)
net_banking = NetBanking(10000)


# Displaying the result of each payment method

print("UPI")
print(upi.payment())

print("\nCredit Card")
print(credit_card.payment())

print("\nDebit Card")
print(debit_card.payment())

print("\nWallet")
print(wallet.payment())

print("\nNet Banking")
print(net_banking.payment())