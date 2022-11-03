"""
Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
Method call car.drive(1.5) increases the travelled distance to 2090 km.
"""

class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerator(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def distance(self, hours_number):
        new_distance = self.current_speed * hours_number
        self.travelled_distance += new_distance


# Main program
car = Car("ABC-123", 142)
car.accelerator(50)
car.distance(3)
car.distance(2)


print(f"{car.travelled_distance}")

