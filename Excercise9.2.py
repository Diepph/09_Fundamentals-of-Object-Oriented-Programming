"""
Extend the program by adding an accerelate method into the new class. The method should receive the change of speed (km/h) as a parameter.
If the change is negative, the car reduces speed. The method must change the value of the speed property of the object.
The speed of the car must stay below the set maximum and cannot be less than zero.
Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
The travelled distance does not have to be updated yet.
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


# Main program
# Create a list of speed acceleration
new_speeds = [30, 70, 50]

# A new object car is created
car = Car("ABC-123", 142)

# Using for loop to update the speed acceleration constantly
for i in new_speeds:
    car.accelerator(i)
print(f"The current speed of the car is: {car.current_speed}")

car.accelerator(-200)
print(f"The final speed of the car is: {car.current_speed}")







