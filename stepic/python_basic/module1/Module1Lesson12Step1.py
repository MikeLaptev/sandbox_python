# coding=utf-8
from math import sqrt

__author__ = "mlaptev"

if __name__ == "__main__":
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
