# coding=utf-8
__author__ = "mlaptev"

north_command = "north"
south_command = "south"
west_command = "west"
east_command = "east"

if __name__ == "__main__":
    amount_of_commands = int(eval(input()))
    x, y = 0, 0
    for _ in range(amount_of_commands):
        command, distance = input().split()
        distance = int(distance)
        if command == north_command:
            y += distance
        elif command == south_command:
            y -= distance
        elif command == west_command:
            x -= distance
        elif command == east_command:
            x += distance
    print(("{} {}".format(x, y)))
