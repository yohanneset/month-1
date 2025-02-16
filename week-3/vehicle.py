
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        return f'This is {self.make} {self.model} vehicle. '


class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    
    def describe(self):
        return f'This is {self.make} {self.model} car. '


class Bike(Vehicle):
    def describe(self):
        return f'This is {self.make} {self.model} bike. '
