"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from car import Car


limo = Car(100, "BMW")

limo.add_fuel(20)
print("fuel =", limo.fuel)

limo.drive(115)
print("odo =", limo.odometer)

print(limo)