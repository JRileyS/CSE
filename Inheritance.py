class Vehicle(object):
    def __init__(self, name):
        self.name = name


class Car(Vehicle):
    def __init__(self, name, milage):
        super(Car, self).__init__(name)
        self.engine_status = False
        self.fuel = 100
        self.milage = milage

    def start_engine(self):
        self.engine_status = True
        print("You start up the car's engine.")

    def move_forward(self):
        self.fuel -= 1
        print("The car moved forward.")

    def move_backward(self):
        self.fuel -= 1
        print("The car moved backwards.")

    def turn_left(self):
        self.fuel -= 1
        print("The car turned left.")

    def turn_right(self):
        self.fuel -= 1
        print("The car turned right.")

    def turn_off(self):
        self.engine_status = False
        print("You turned off the car.")


class Impala(Car):
    def __init__(self):
        super(Impala, self).__init__("Impala", 25)


thanos_car = Impala()
thanos_car.start_engine()
thanos_car.move_forward()
thanos_car.turn_left()
thanos_car.move_backward()
thanos_car.turn_off()

class KeylessCar(Car):
    def __init__(self, name, milage):
        super(KeylessCar, self).__init__(name, milage)

    def start_engine(self):
        self.engine_status = True
        print("You push the button and the car turns on.")


wiebe_car = KeylessCar("Tesla", 125)
wiebe_car.start_engine()
wiebe_car.move_forward()
wiebe_car.turn_left()
wiebe_car.move_backward()
wiebe_car.turn_off()