from vehicles.makes import Vehicle

class Nissan(Vehicle):
    def __init__(self, color, occupancy, name):
        super().__init__(color, occupancy, name)

    def drive(self):
        print(f"The {self.main_color} Nissan drives past. RRrrrrrummbbble!")
        self.is_driving = True