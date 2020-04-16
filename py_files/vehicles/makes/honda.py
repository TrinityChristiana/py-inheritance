from vehicles.makes import Vehicle
import json

positions = ["north", "east", "south", "west"]

class Honda(Vehicle):
    def __init__(self, color, occupancy, name):
        super().__init__(color, occupancy, name)

    def drive(self):
        print(f"The {self.main_color} Honda drives past. RRrrrrrummbbble!")
        self.is_driving = True

    def stop(self): 
        if self.is_driving:
            self.is_driving = False
            print(f"{self.name} smoothly stops and is now facing {self.direction}")
        else:
            print(f"{self.name} is already stopped and is facing {self.direction}") 
