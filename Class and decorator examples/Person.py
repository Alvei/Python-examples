""" person.py
    Inspired from https://realpython.com/python-data-classes/ """
from dataclasses import dataclass, field, fields
from math import asin, cos, radians, sin, sqrt

EARTH_RADIUS = 6371                             # Earth radius in kilometers

@dataclass
class Person:
    """ Person with name and age attributes. """
    name: str
    age: int

    def celebrate_birthday(self) -> None:
        """ Adds a year to the instance of the class. """
        self.age += 1

@dataclass
class Position:
    """ Position of a point with longitude and lattitude. Use field() to set default. """
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

    def distance_to(self, other):
        """ Calculate the distance between one position and another, along the Earth’s
            surface using the haversine formula. """

        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        radicand = (sin((phi_2 - phi_1) / 2)**2
                    + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * EARTH_RADIUS * asin(sqrt(radicand))

@dataclass
class Capital(Position):
    """ Position of a Capital with longitude and lattitude. If a parameter has
        a default value, all following parameters must also have a default value. In
        other words, if a field in a base class has a default value, then all new fields
        added in a subclass must have default values as well.Use field() to set default. """
    country: str = field(default='Na')

def main():
    """ Test harness. """
    jdoe = Person('John Doe', 42)
    jdoe.celebrate_birthday()
    print(jdoe)

    print(Position('Null Island'))
    oslo = Capital('Oslo', 10.8, 59.9, 'Norway')
    vancouver = Position('Vancouver', -123.1, 49.3)
    print(f"Distance from {oslo.name} to {vancouver.name}: {oslo.distance_to(vancouver):.2f} Km")
    lat_unit = fields(Position)[2].metadata['unit']
    print(f"Latitude Unites: {lat_unit}")

    print(f"{oslo.name} is the capital of {oslo.country}")


if __name__ == "__main__":
    main()
