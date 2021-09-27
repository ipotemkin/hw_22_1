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

    def sleep(self):
        print('Кот спит')

    def run(self):
        print(
            'Пусть кажется что кот просто лежит на диване, '
            'но на самом деле он мчится через вселенную с умопомрачительной скоростью ')


class Tiger(AbstractCat):
    def meow(self):
        print('РРРР!')

    def sleep(self):
        print('Тигр спит')

    def run(self):
        print('Тигр бежит со скоростью 67 км\ч')


# Корректное использование абстрактных классов
cat = Cat()
tiger = Tiger()

# Так же можно проверить,
# что объект передаваемый в качестве аргумента является реализацией необходимого абстрактного класса

print(isinstance(tiger, AbstractCat))
print(isinstance(cat, AbstractCat))