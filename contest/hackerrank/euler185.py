#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 12


def precompute(queries):
    choices = [[] for _ in range(N)]

    def test(idx, c):
        for q, v in queries:
            if q[idx] == c and v == 0:
                return False
        return True

    for i in range(N):
        opts = []
        for c in '0123456789':
            if test(i, c):
                opts.append(c)
        choices[i] = opts
    return choices


def run(queries):
    n = len(queries)
    queries = [(x, int(y)) for (x, y) in queries]
    cs = [0] * n
    queries.sort(key=lambda x: x[1])
    choices = precompute(queries)

    def test(idx, c):
        j = -1
        for i in range(n):
            if queries[i][0][idx] == c:
                cs[i] += 1
            if cs[i] > queries[i][1] or (cs[i] + (N - idx - 1)) < queries[i][1]:
                j = i
                break
        if j != -1:
            for i in range(j + 1):
                if queries[i][0][idx] == c:
                    cs[i] -= 1
            return False
        return True

    def roll(idx, c):
        for i in range(n):
            if queries[i][0][idx] == c:
                cs[i] -= 1

    path = []

    def dfs():
        if len(path) == N:
            return True

        opts = choices[len(path)]
        for c in opts:
            if test(len(path), c):
                path.append(c)
                if dfs():
                    return True
                path.pop()
                roll(len(path), c)

        return False

    dfs()
    ans = ''.join(path)
    return ans


# this is codeforces main function
def main():
    from sys import stdin

    def read_int():
        return int(stdin.readline())

    def read_int_array(sep=None):
        return [int(x) for x in stdin.readline().split(sep)]

    def read_str_array(sep=None):
        return [x.strip() for x in stdin.readline().split(sep)]

    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')

    while True:
        try:
            n = read_int()
            break
        except:
            pass

    queries = []
    for i in range(n):
        queries.append(read_str_array())
    ans = run(queries)
    print(ans)


if __name__ == '__main__':
    main()
