class Person:
    def __init__(self, city_population, room_num):
        self.city_popultaion = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.planet.get_contry().get_city().get_street().get_room().get_name()

    def get_city_population(self):
        return self.planet.get_contry().get_city().population()