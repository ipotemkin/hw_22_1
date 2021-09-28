from abc import ABC, abstractmethod


class AbstractCat(ABC):

    @abstractmethod
    def meow(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Cat(AbstractCat):

    def meow(self):
        print('мяу')

    def run(self):
        print(
            'Пусть кажется что кот просто лежит на диване, '
            'но на самом деле он мчится через вселенную с умопомрачительной скоростью ')


# Класс наследник абстрактного класса должен реализовывать все методы помеченные декоратором @abstractmethod.
# При попытке выполнить этот код будет выброшено исключение TypeError
cat = Cat()
