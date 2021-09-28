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


# Абстрактный класс не может иметь экземпляров. При попытке выполнить этот код будет выброшено исключение TypeError
cat = AbstractCat()
