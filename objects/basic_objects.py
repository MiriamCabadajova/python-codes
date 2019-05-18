from math import sqrt, pi


class Rectangle:
    __slots__ = "width", "height"

    def __init__(self, width, height):
        self.width = width
        self.height = height


def area(rec):
    return rec.width * rec.height


class Point:
    __slots__ = "x", "y"

    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)


class Book:
    __slots__ = "name", "author", "ISBN", "price"

    def __init__(self, name, author, ISBN, price):
        self.name = name
        self.author = author
        self.ISBN = ISBN
        self.price = price


def print_info(name_of_book):
    print("name:   ", name_of_book.name)
    print("author: ", name_of_book.author)
    print("isbn:   ", name_of_book.ISBN)
    print("price:  ", "$", name_of_book.price)


class Circle:
    __slots__ = "center", "radius"

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def get_perimeter(self):
        return self.radius * 2 * pi

    def get_area(self):
        return self.radius ** 2 * pi

    def __str__(self):
        a = ("Circle at centre " + str(self.center) + " with radius " + str(self.radius))
        return a


class Square:
    __slots__ = "center", "side"

    def __init__(self, center, side):
        self.center = center
        self.side = side

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2

    def __str__(self):
        return "Square at centre " + str(self.center) + " with side " + str(self.side)


class Triangle:
    __slots__ = "center", "side"

    def __init__(self, center, side):
        self.center = center
        self.side = side

    def get_perimeter(self):
        return self.side * 3

    def get_area(self):
        return self.side ** 2 * (sqr(3) / 4)

    def __str__(self):
        return "Triangle at centre " + str(self.center) + " with side " + str(self.side)


class Creature:

    def __init__(self, name, level, health_max):
        self.name = name
        self.level = level
        self.health_max = health_max

    def __str__(self):
        return ("Creature is called " + str(self.name) + ", current level is " + str(
            self.level) + " and the health max is " + str(self.health_max) + ".")

    def get_level(self):
        return self.level

    def new_level(self):
        a = self.level + 1
        return a

    @staticmethod
    def attack(enemy):
        if enemy.level > creature.level:
            creature.undertake_attack((enemy.level - creature.level) * 100)
        print(creature)
        enemy.new_level()
        print(enemy)

    def undertake_attack(self, damage):
        self.health_max -= damage


test_creature = Creature("Jerry", 2, 1500)
test_enemy = Creature("ll", 6, 1400)
