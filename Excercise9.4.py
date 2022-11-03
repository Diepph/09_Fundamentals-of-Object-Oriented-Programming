"""
Now we will program a car race. The travelled distance of a new car is initialized as zero.
At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
One per every hour of the race, the following operations are performed:
The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
This is done using the accerelate method.
Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers.
Finally, the properties of each car are printed out formatted into a clear table.
"""
import random
from prettytable import PrettyTable

class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = maximum_speed
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
list = []
distance_goal = 10000

# Generate ten cars using for loop
for i in range(10):
    registration_number = ("ABC-" + "%d") % (i + 1)
    # Generate random speed for each car
    random_max_speed = random.randint(100, 200)
    list.append(Car(registration_number, random_max_speed))


# Let the cars race
while True:
    condition = 0
    for car in list:
        x = 0
        random_change_speed = random.randint(-10, 15)
        car.accelerator(random_change_speed)
        car.distance(1)
        if car.travelled_distance >= distance_goal:
            condition = 1

    if condition == 1:
        break


table = PrettyTable(['Registration number', 'Maximum speed', 'Current speed', 'Travelled distance'])

for car in list:
    table.add_row([car.registration_number, car.current_speed, car.maximum_speed, car.travelled_distance])
print(table)

