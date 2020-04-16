from vehicles.makes import Vehicle

class Kia(Vehicle):
    def __init__(self, color, occupancy, name):
        super().__init__(color, occupancy, name)

    def drive(self):
        print(f"The {self.main_color} Kia is broken down, you cannot drive this lemon")

    def turn(self, direction):
        self._direction = direction

    def stop(self):
        print(f"{self.name}'s already stopped and is now facing {self.direction}")