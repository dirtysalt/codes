#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 12


def precompute(queries):
    n = len(queries)

    # rows[i][c] 在ith上面选择c的话，有哪些行是可以匹配的
    rows = [[[] for _ in range(10)] for _ in range(N)]
    for i in range(N):
        for c in range(10):
            for j in range(n):
                if queries[j][0][i] == c:
                    rows[i][c].append(j)

    choices = [[] for _ in range(N)]
    exclude = [[0] * 10 for _ in range(N)]
    qs = [q for (q, c) in queries if c == 0]
    for q in qs:
        for i in range(N):
            exclude[i][q[i]] = 1

    # 第ith可以选择的数字
    for i in range(N):
        opts = []
        for c in range(10):
            if exclude[i][c] == 0:
                opts.append(c)
        choices[i] = opts

    choices = [(i, choices[i]) for i in range(N)]

    # 字符搜索次序，尽可能优先使用匹配多行的
    for idx, opts in choices:
        opts.sort(key=lambda x: -len(rows[idx][x]))

    # 按照可选数字的多少做排序, 优先使用数字少的
    # 相同情况下面，选择这个总体匹配多行的
    # 调整搜索顺序可能是比较关键的
    # choices.sort(key=lambda x: (len(x[1]), -sum((len(rows[x[0]][c]) for c in x[1]))))
    choices.sort(key=lambda x: -sum((len(rows[x[0]][c]) for c in x[1])) / (len(x[1]) ** 2))
    return choices, rows


def run(queries):
    queries = [([int(c) for c in x], int(y)) for (x, y) in queries]
    choices, rows = precompute(queries)
    # print(choices)

    n = len(queries)
    correct = [0] * n

    def test(idx, c, k):
        for i in rows[idx][c]:
            correct[i] += 1

        for i in range(n):
            if correct[i] > queries[i][1] or (correct[i] + (N - k - 1)) < queries[i][1]:
                return False
        return True

    def rollback(idx, c):
        for i in rows[idx][c]:
            correct[i] -= 1

    path = [None] * N

    def dfs(k):
        if k == N:
            return True

        idx, opts = choices[k]
        for c in opts:
            ok = test(idx, c, k)
            if ok:
                path[idx] = c
                if dfs(k + 1):
                    return True
                path[idx] = None
            rollback(idx, c)

        return False

    assert dfs(0)
    ans = ''.join([str(x) for x in path])
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
