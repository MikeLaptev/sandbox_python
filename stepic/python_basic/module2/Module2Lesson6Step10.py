# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    matrix = []
    line = input()
    while line != 'end':
        matrix.append([int(i) for i in line.split()])
        line = input()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i-1][j] + matrix[(i+1)%len(matrix)][j] + matrix[i][j-1] + matrix[i][(j+1)%len(matrix[i])],
                  end=' ')
        print()
