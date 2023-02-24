import json

# TODO
# Debug car name in santica..done
#   code was correct, names sanica + santro = santro (according to name logic ;-})
# Try __add__ with three args

class Car:
    def __init__(self, name, engine, fuel_type) -> None:
        self.name = name
        self.engine = engine
        self.fuel_type = fuel_type

    def __add__(self, car):
        return Car(
            self.name[:len(self.name)//2] + car.name[len(car.name)//2:],
            self.engine + car.engine,
            self.fuel_type + car.fuel_type)
    
    def car_details(self):
        print("Car: {}\nEngine: {}\nFuel type: {}\n".format(self.name, self.engine, self.fuel_type))
    
santro = Car("Santro", 800, 'petrol')
indica = Car("Indica", 850, 'diesel')
santro.car_details()
indica.car_details()
####

santica = santro + indica + santro
print("SAN:", santica.car_details())
santica = santica + santro
print(santica)
santica.car_details()