from math import sin, pi

__author__ = 'mlaptev'


def calculate_by_position(n):
    return (-9)**((n-sin(n*pi/2)**2)/2)


def generate_value(till):
    step = 2
    intermediate_step = 1
    latest_value = 1
    for i in range(till):
        if i == 0 or i == 1:
            yield latest_value
        else:
            yield -9*latest_value
            if intermediate_step == step:
                latest_value *= -9
                intermediate_step = 1
            else:
                intermediate_step += 1


if __name__ == "__main__":
    for position, value in enumerate(generate_value(15)):
        print(calculate_by_position(position), value)
