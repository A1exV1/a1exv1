from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    def distance(self, other):
        cos_d = (sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) *
                 cos(self.longitude - other.longitude))
        return 6371 * acos(cos_d)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height


moscow = City(55.755864, 37.617698, 'Москва', 20000000)
everest = Mountain(27.988056, 86.925278, 'Эверест', 8848)

print(int(moscow.distance(everest)))
