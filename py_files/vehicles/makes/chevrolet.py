from vehicles.makes import Vehicle

positions = ["north", "east", "south", "west"]

class Chevrolet(Vehicle):
    def __init__(self, color, occupancy, name):
        super().__init__(color, occupancy, name)

    def drive(self):
        print(f"The {self.main_color} Chevrolet drives past. RRrrrrrummbbble!")
        self.is_driving = True

    def stop(self):
        if self.is_driving:
            self.is_driving = False
            print(f"It takes a min for the tires to stop, but eventually {self.name} stops and is now facing {self.direction}")
        else:
            print(f"{self.name} is already stopped and is facing {self.direction}") 

        