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
        self.flight_vehicle = FlightVehicle()

# [Vehicle] has a [FlightVehicle]
class FlightVehicle:
    def __init__(self):
        self.starship = Starship()

# [FlightVehicle] has a [Starship]
class Starship:
    pass

# [Airplane] is a [FlightVehicle]
class Airplane(FlightVehicle):
    pass

# [GroundVehicle] is a [Vehicle]
class GroundVehicle(Vehicle):
    pass

# [Car] is a [GroundVehicle]
class Car(GroundVehicle):
    pass

# [Motorcycle] is a [GroundVehicle]
class Motorcycle(GroundVehicle):
    pass



