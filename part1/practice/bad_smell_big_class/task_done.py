class Base:
    @classmethod
    def get_name(cls):
        return cls.__name__

    @classmethod
    def get_methods(cls):
        return ', '.join([method for method in cls.__dict__ if method.startswith('__') is False])

    def __repr__(self):
        return f"I'm {self.get_name()}, I can {self.get_methods()}"


class Object(Base):
    def defense(self):
        pass


class Person(Object):
    def move(self):
        pass


class Warrior(Person):
    def attack(self):
        pass


class Healer(Person):
    def heal(self):
        pass


class Tree(Object):
    def on_fire(self):
        pass


class Trap(Base):
    def attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    obj = Object()
    print(obj)

    person = Person()
    print(person)

    hero = Healer()
    print(hero)

    warrior = Warrior()
    print(warrior)

    tree = Tree()
    print(tree)

    trap = Trap()
    print(trap)
