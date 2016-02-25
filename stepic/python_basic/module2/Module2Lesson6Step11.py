# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    amount = int(input())
    all_numbers = [i for i in range(1, amount**2 + 1)]
    spiral = [[-1 for _ in range(amount)] for _ in range(amount)]
    vertical_min, vertical_max, vertical_direction, vertical_position = -1, amount, 0, 0
    horizon_min, horizon_max, horizon_direction, horizon_position = -1, amount, 1, 0
    for number in all_numbers:
        if horizon_position + horizon_direction > horizon_max:
            # update position
            horizon_position -= 1
            vertical_position += 1
            # update direction
            horizon_direction = 0
            vertical_direction = 1
            # update border
            vertical_min += 1
        if vertical_position + vertical_direction > vertical_max:
            # update position
            vertical_position -= 1
            horizon_position -= 1
            # update direction
            horizon_direction = -1
            vertical_direction = 0
            # update border
            horizon_max -= 1
        if horizon_position + horizon_direction < horizon_min:
            # update position
            horizon_position += 1
            vertical_position -= 1
            # update direction
            horizon_direction = 0
            vertical_direction = -1
            # update border
            vertical_max -= 1
        if vertical_position + vertical_direction < vertical_min:
            # update position
            vertical_position += 1
            horizon_position += 1
            # update direction
            horizon_direction = 1
            vertical_direction = 0
            # update border
            horizon_min += 1
        spiral[vertical_position][horizon_position] = number
        horizon_position += horizon_direction
        vertical_position += vertical_direction
    for line in spiral:
        print(" ".join([str(i) for i in line]))
