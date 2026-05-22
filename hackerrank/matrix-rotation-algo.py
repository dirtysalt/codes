#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

def rotate(mx, i, j, n, m, r):
    # print(i, j, n, m)
    path = []
    x, y, d = i, j, 0
    while True:
        path.append((x, y))
        if d == 0 and x == (n - 1 + i):
            d = 1
        if d == 1 and y == (m - 1 + j):
            d = 2
        if d == 2 and x == i:
            d = 3

        if d == 0:
            x += 1
        elif d == 1:
            y += 1
        elif d == 2:
            x -= 1
        else:
            y -= 1
            if y == j:
                break

    sz = len(path)
    r = r % sz
    values = [mx[x][y] for (x, y) in path]
    for i, (x, y) in enumerate(path):
        idx = (i - r + sz) % sz
        mx[x][y] = values[idx]


# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    n, m = len(matrix), len(matrix[0])
    i, j = 0, 0
    while n > 0 and m > 0:
        rotate(matrix, i, j, n, m, r)
        n -= 2
        m -= 2
        i += 1
        j += 1

    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        print(' '.join([str(x) for x in matrix[i]]))


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
