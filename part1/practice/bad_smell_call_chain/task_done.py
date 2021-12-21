class Person:
    def __init__(self, city_population: int, room_number: int):
        self.city_population = city_population
        self.room_number = room_number

    def get_person_room(self):
        return self.room_number

    def get_city_population(self):
        return self.city_population


if __name__ == '__main__':
    person = Person(city_population=100_500, room_number=42)

    print("My room is", person.get_person_room())
    print("My city's population is", person.get_city_population())
