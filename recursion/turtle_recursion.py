from turtle import Turtle
from math import sqrt

julie = Turtle()
julie.speed(10)


def draw_square(turtle, length):
    """
    Function which draws a simple square

    :param turtle: instance of Turtle object
    :param length: size of one side of the square

    """
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


# print(draw_square(julie, 100))


def nested_squares(depth, length):
    """
    Recursive function which draws nested squares
    :param depth: the depth of recursion
    :param length: size of one side of the largest square
    """
    if depth == 0:
        return
    else:
        draw_square(julie, length)
        julie.forward(length // 2)
        julie.right(45)
        nested_squares(depth - 1, length / sqrt(2))


# print(nested_squares(10, 100))

julie.left(90)


def tree(length):
    """
    Recursive function which draws a tree
    :param length: size of the tree
    """
    julie.forward(length)
    if length > 10:
        julie.left(45)
        tree(0.6 * length)
        julie.right(90)
        tree(0.6 * length)
        julie.left(45)
    julie.back(length)


# print(tree(120))

julie.right(90)


def koch(depth, length):
    """
    Function which draws koch's snowflake
    :param depth: depth of recursion
    :param length: size of a side
    """
    if depth == 0:
        julie.forward(length)
    else:
        koch(depth - 1, length / 3)
        julie.left(60)
        koch(depth - 1, length / 3)
        julie.right(120)
        koch(depth - 1, length / 3)
        julie.left(60)
        koch(depth - 1, length / 3)

# print(koch(5,300))
