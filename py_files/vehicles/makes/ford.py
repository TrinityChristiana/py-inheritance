from vehicles.makes import Vehicle

class Ford(Vehicle):
    def __init__(self, color, occupancy, name):
        super().__init__(color, occupancy, name)

    def open_hatch_back(self):
        print()

    def drive(self):
        print(f"The {self.main_color} Ford drives past. RRrrrrrummbbble!")
        self.is_driving = True

    