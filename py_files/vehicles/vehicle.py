import random
import json

positions = ["north", "east", "south", "west"]


class Vehicle:
    """
    Methods:
    drive()
    """

    def __init__(self, color, occupancy, name):
        """
        color - color of vehicle
        occupancy = number of seats
        """
        self.main_color = color
        self.maximum_occupancy = occupancy
        self.name = name
        self.direction = "north"
        self.is_driving = False

    def drive(self):
        print("Vroooom!")
        self.is_driving = True

    @property
    def direction(self):
        try:
            return self.__direction
        except AttributeError:
            return 0

    @direction.setter
    def direction(self, direction):
        if self.direction == 0:
            self.__direction = direction
        else:
            try:
                if type(direction) == str:
                    direction_in = positions.index(self.direction)
                    next_pos = positions[direction_in + 1] if direction_in + 1 >= 0 and direction_in + 1 < len(
                        positions) else positions[0]
                    past_pos = positions[direction_in - 1]

                    print(past_pos, self.direction, next_pos)

                    if direction == next_pos or direction == past_pos or direction == self.direction:
                        self.__direction = direction
                    else:
                        raise TypeError(
                            f"Current options of directions are {past_pos} {self.direction} and {next_pos}")
                else:
                    raise TypeError(
                        "Please provide a string as a value of direction")
            except TypeError as taco:
                print(f"TypeError: {taco}")

    def turn(self, direction):
        if not self.is_driving:
            print(f"{self.name} is not driving yet, start driving before turning")
        else:
            direction_in = positions.index(self.direction)
            next_pos = positions[direction_in + 1] if direction_in + 1 >= 0 and direction_in + 1 < len(
            positions) else positions[0]
            past_pos = positions[direction_in - 1]

            if direction == "left":
                self.__direction = past_pos

            if direction == "right":
                self.__direction = next_pos

            if direction == "straight":
                self.__direction = self.direction

    def stop(self):
        if self.is_driving:
            self.is_driving = False
            print(f"{self.name} stops and is now facing {self.direction}")
        else:
            print(f"{self.name} is already stopped and is facing {self.direction}")            

    def fill_tank(self):
        print(f"{self.name} loves the food")

    def wash_car(self):
        num = random.choice([i for i in range(100)])
        if num == 66:
            print(f"{self.name}'s {self.main_color} paint now glissens in the rain")
        else:
            print(
                f"{self.name}'s {self.main_color} paint noe glissens in the sunlight")

    def print_details(self):
        print(json.dumps(self.__dict__, indent=2))
