# ============================================================
# OOP Exercise 1: Create a Class with instance attributes
# ------------------------------------------------------------
# Question:
# Write a Python program to create a Vehicle class with
# max_speed and mileage instance attributes.
#
# Expected Output:
# Max Speed: 180
# Mileage: 12
# ============================================================

class Vehicle:
    def __init__(self, max_speed, mileage):
        # instance attributes
        self.max_speed = max_speed
        self.mileage = mileage

# creating object
car = Vehicle(180, 12)

print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)


# ============================================================
# OOP Exercise 2: Create a Vehicle class without variables
# and methods
# ------------------------------------------------------------
# Question:
# Create a Vehicle class without any variables and methods.
# ============================================================

class Vehicle:
    pass  # empty class using pass keyword


# ============================================================
# OOP Exercise 3: Create a child class Bus
# ------------------------------------------------------------
# Question:
# Create a child class Bus that will inherit all variables
# and methods of the Vehicle class.
#
# Given:
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# Expected Output:
# Vehicle Name: School Volvo
# Speed: 180
# Mileage: 12
# ============================================================

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass  # inherits everything from Vehicle

# creating Bus object
school_bus = Bus("School Volvo", 180, 12)

print("Vehicle Name:", school_bus.name)
print("Speed:", school_bus.max_speed)
print("Mileage:", school_bus.mileage)


# ============================================================
# OOP Exercise 4: Class Inheritance with default argument
# ------------------------------------------------------------
# Question:
# Create a Bus class that inherits from Vehicle.
# Give seating_capacity() default value of 50.
#
# Expected Output:
# The seating capacity of a bus is 50 passengers
# ============================================================

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        # overriding method with default value
        return super().seating_capacity(capacity)

bus = Bus("bus", 180, 12)
print(bus.seating_capacity())


# ============================================================
# OOP Exercise 5: Class attribute (same for all objects)
# ------------------------------------------------------------
# Question:
# Define a class attribute "color" with default value White.
#
# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
# ============================================================

class Vehicle:
    color = "White"  # class attribute (same for all objects)

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)

print(f"Color: {bus.color}, Vehicle name: {bus.name}, Speed: {bus.max_speed}, Mileage: {bus.mileage}")
print(f"Color: {car.color}, Vehicle name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}")


# ============================================================
# OOP Exercise 6: Override method and calculate fare
# ------------------------------------------------------------
# Question:
# Default fare = capacity * 100
# If vehicle is Bus, add extra 10% maintenance charge
#
# Bus capacity = 50
# Final Fare = 5500
#
# Expected Output:
# Total Bus fare is: 5500.0
# ============================================================

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        # base fare calculation
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        # calling parent fare method
        base_fare = super().fare()
        # adding 10% maintenance charge
        return base_fare + (base_fare * 0.10)

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# ============================================================
# OOP Exercise 7: Check type of an object
# ------------------------------------------------------------
# Question:
# Determine which class a given Bus object belongs to.
# ============================================================

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# checking object type
print(type(School_bus))


# ============================================================
# OOP Exercise 8: Check if object is instance of Vehicle
# ------------------------------------------------------------
# Question:
# Determine if School_bus is also an instance of Vehicle class.
#
# Expected Output:
# True
# ============================================================

print(isinstance(School_bus, Vehicle))


# ============================================================
# OOP Exercise 9: Multiple Inheritance & MRO (TOUGH)
# ------------------------------------------------------------
# Question:
# Create two parent classes Engine and ElectricFeature.
# Engine should have method engine_type().
# ElectricFeature should have method battery_capacity().
#
# Create a child class ElectricCar that inherits from both.
# Use super() properly and print complete car information.
#
# Given:
# Engine type = "Electric Motor"
# Battery Capacity = "75 kWh"
#
# Expected Output:
# Engine Type: Electric Motor
# Battery Capacity: 75 kWh
# ============================================================

class Engine:
    def engine_type(self):
        return "Electric Motor"

class ElectricFeature:
    def battery_capacity(self):
        return "75 kWh"

class ElectricCar(Engine, ElectricFeature):
    def car_details(self):
        # accessing methods from both parent classes
        print("Engine Type:", self.engine_type())
        print("Battery Capacity:", self.battery_capacity())

# creating object
tesla = ElectricCar()
tesla.car_details()

# ============================================================
# OOP Exercise 10: Encapsulation using @property (TOUGH)
# ------------------------------------------------------------
# Question:
# Create a BankAccount class.
# Make balance a private variable.
# Use @property to get balance.
# Use setter to prevent negative balance.
#
# Given:
# Initial balance = 5000
# Deposit = 2000
# Withdraw = 3000
#
# Expected Output:
# Current Balance: 7000
# Current Balance: 4000
# ============================================================

class BankAccount:
    def __init__(self, balance):
        # private variable using name mangling
        self.__balance = balance

    @property
    def balance(self):
        # getter method
        return self.__balance

    @balance.setter
    def balance(self, amount):
        # setter with validation
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = amount

    def deposit(self, amount):
        # increasing balance
        self.balance = self.balance + amount
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        # decreasing balance safely
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Current Balance:", self.balance)

# creating object
account = BankAccount(5000)

account.deposit(2000)
account.withdraw(3000)

# ==================== COMPLETED ================== #