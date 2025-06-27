# coding=utf-8
from math import sqrt

__author__ = "mlaptev"

if __name__ == "__main__":
    triangle_room = "треугольник"
    rectangle_room = "прямоугольник"
    circle_room = "круг"
    room_type = eval(input())
    if room_type == triangle_room:
        first_side = int(eval(input()))
        second_side = int(eval(input()))
        third_side = int(eval(input()))
        semi_perimeter = (first_side + second_side + third_side) / 2
        print(
            (
                sqrt(
                    semi_perimeter
                    * (semi_perimeter - first_side)
                    * (semi_perimeter - second_side)
                    * (semi_perimeter - third_side)
                )
            )
        )
    elif room_type == rectangle_room:
        first_side = int(eval(input()))
        second_side = int(eval(input()))
        print((first_side * second_side))
    elif room_type == circle_room:
        radius = int(eval(input()))
        print((3.14 * radius * radius))
