# Task 24
import abc

class Vehicle:

    @abc.abstractmethod
    def drive_direction(self):
        pass

class Car(Vehicle):

    def drive_direction(self):
        return "Drive forward"

class Plane(Vehicle):

    def drive_direction(self):
        return "Drive Upward"

vehicle_direction= Vehicle()
print(vehicle_direction.drive_direction())

car_direction= Car()
print(car_direction.drive_direction())

plane_direction= Plane()
print(plane_direction.drive_direction())