# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class:
class Vehicle:
    def __init__(self):
        pass

# [Vehicle] has a [FlightVehicle]
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# [FlightVehicle] has a [Starship]
class Starship(FlightVehicle):
    def __init__(self):
        pass

# [Airplane] is a [FlightVehicle]
class Airplane(FlightVehicle):
    def __init__(self):
        pass

# [GroundVehicle] is a [Vehicle]
class GroundVehicle(Vehicle):
    def __init__(self):
        pass

# [Car] is a [GroundVehicle]
class Car(GroundVehicle):
    def __init__(self):
        pass

# [Motorcycle] is a [GroundVehicle]
class Motorcycle(GroundVehicle):
    def __init__(self):
        pass
