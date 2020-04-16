# **************************** Challenge: Custom Colors and Sounds ****************************
 
'''
Author: Trinity Terry
pyrun: python main.py
'''
from vehicles import Chevrolet, Ford, Honda, Kia, Nissan
# from py_files.vehicles import Chevrolet

# Define 5 of your favorite vehicles
# Move all common properties in your vehicles to a new Vehicle class.
# Create an instance of each vehicle.
# Define a different value for each vehicle's properties.
# Create a drive() method in the Vehicle class.
# Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
# Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
# Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
# Make your vehicle instances perform all three behaviors.

mocha = Honda("brown", 5, "Mocha")
sentra = Nissan("green", 5, "Sentra") 
big_boy = Chevrolet("black", 5, "Big Boy")
bat_mobile = Ford("black", 5, "Bat Mobile")
broke = Kia("orange", 5, "Broken")

print("\n", "********** Mocha **********")
mocha.drive()
mocha.turn("right")
mocha.turn("left")
mocha.turn("straight")
mocha.stop()
mocha.stop()


print("\n", "********** Sentra **********")
sentra.drive()
sentra.turn("right")
sentra.turn("left")
sentra.turn("straight")
sentra.stop()
sentra.stop()


print("\n", "********** Big Boy **********")
big_boy.drive()
big_boy.turn("right")
big_boy.turn("left")
big_boy.turn("straight")
big_boy.stop()
big_boy.stop()

print("\n", "********** Broke **********")
broke.drive()
broke.turn("right")
broke.turn("left")
broke.turn("straight")
broke.stop()
broke.stop()

print("\n", "********** Bat Mobile **********")
bat_mobile.drive()
bat_mobile.turn("right")
bat_mobile.turn("left")
bat_mobile.turn("straight")
bat_mobile.stop()
bat_mobile.stop()
