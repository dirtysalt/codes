#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

import os


# Complete the gridSearch function below.
def gridSearch(G, P):
    R, C = len(G), len(G[0])
    r, c = len(P), len(P[0])

    for i in range(0, R - r + 1):
        for j in range(0, C - c + 1):
            # print('>>>', c,j, G[i][j:j+c], '>>>', P[0])
            if G[i][j:j + c] == P[0]:
                ok = True
                for sz in range(1, r):
                    if G[i + sz][j:j + c] != P[sz]:
                        ok = False
                        break
                if ok:
                    return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
