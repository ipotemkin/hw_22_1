from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    def start_engine(self):
        print("Двигатель катера запущен")

    def stop_engine(self):
        print("Двигатель катера остановлен")

    def move(self):
        print("Катер плывет!")

    def stop(self):
        print("Катер остановился")


class Car(Transport):
    def start_engine(self):
        print("Двигатель машины запущен")

    def stop_engine(self):
        print("Двигатель машины остановлен")

    def move(self):
        print("Машина едет")

    def stop(self):
        print("Машина остановилась")


class ElectroScooter(Transport):
    def start_engine(self):
        print("Двигатель скутера запущен")

    def stop_engine(self):
        print("Двигатель скутера остановлен")

    def move(self):
        print("Скутер едет")

    def stop(self):
        print("Скутер остановился")


class Person:
    @staticmethod
    def use_transport(transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()


if __name__ == '__main__':
    car = Car()
    boat = Boat()
    scooter = ElectroScooter()
    person = Person()
    person.use_transport(car)
    person.use_transport(boat)
    person.use_transport(scooter)
